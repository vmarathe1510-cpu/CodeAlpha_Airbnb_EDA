from pathlib import Path
import warnings
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"
PROCESSED = ROOT / "data" / "processed"
TABLES = ROOT / "outputs" / "tables"
FIGURES = ROOT / "outputs" / "figures"
EXPECTED = ["id", "price", "room_type", "neighbourhood_group",
            "number_of_reviews", "availability_365"]

def price_to_numeric(series):
    cleaned = series.astype("string").str.replace(r"[$,]", "", regex=True).str.strip()
    return pd.to_numeric(cleaned, errors="coerce")

def main():
    for p in [PROCESSED, TABLES, FIGURES]:
        p.mkdir(parents=True, exist_ok=True)
    candidates = [RAW / "listings.csv.gz", RAW / "listings.csv"]
    source = next((p for p in candidates if p.exists()), None)
    if source is None:
        raise FileNotFoundError("Download detailed NYC listings.csv.gz from https://insideairbnb.com/get-the-data/ and save it in data/raw/")
    df = pd.read_csv(source, low_memory=False, compression="infer")
    df.columns = df.columns.astype(str).str.strip()
    print(f"Source: {source}\\nRows: {len(df):,}; columns: {len(df.columns):,}")

    profile = pd.DataFrame({
        "column": df.columns,
        "dtype": [str(df[c].dtype) for c in df.columns],
        "missing_count": [int(df[c].isna().sum()) for c in df.columns],
        "missing_pct": [(df[c].isna().mean()*100).round(2) for c in df.columns],
        "distinct_non_null": [int(df[c].nunique(dropna=True)) for c in df.columns],
    })
    profile.to_csv(TABLES / "column_profile.csv", index=False)

    quality = {
        "rows_loaded": len(df), "columns_loaded": len(df.columns),
        "duplicate_full_rows": int(df.duplicated().sum()),
        "missing_expected_fields": ", ".join(c for c in EXPECTED if c not in df.columns),
        "missing_listing_id": int(df["id"].isna().sum()) if "id" in df else np.nan,
        "duplicate_listing_ids": int(df["id"].duplicated().sum()) if "id" in df else np.nan,
    }
    out = df.copy()
    if "price" in out:
        out["price"] = price_to_numeric(out["price"])
        quality["price_missing_or_unparseable"] = int(out["price"].isna().sum())
        quality["price_zero_or_negative"] = int((out["price"] <= 0).fillna(False).sum())
    pd.DataFrame([quality]).to_csv(TABLES / "data_quality_summary.csv", index=False)

    for col in ["minimum_nights", "number_of_reviews", "reviews_per_month", "availability_365"]:
        if col in out:
            out[col] = pd.to_numeric(out[col], errors="coerce")
    if "last_review" in out:
        out["last_review"] = pd.to_datetime(out["last_review"], errors="coerce")
    if "id" in out:
        out = out.drop_duplicates(subset=["id"], keep="first")
    out.to_csv(PROCESSED / "listings_cleaned.csv", index=False)

    sns.set_theme(style="whitegrid", context="notebook")
    if "price" in out:
        valid = out.loc[out["price"].notna() & (out["price"] > 0)].copy()
        if not valid.empty:
            q99 = valid["price"].quantile(.99)
            valid["price"].describe(percentiles=[.25,.5,.75,.9,.95,.99]).to_frame("value").to_csv(TABLES / "price_summary.csv")
            pd.DataFrame([{
                "valid_price_rows": len(valid), "p99_threshold": q99,
                "rows_above_p99": int((valid["price"] > q99).sum()),
                "median_raw": valid["price"].median(), "mean_raw": valid["price"].mean(),
                "median_capped_p99": valid["price"].clip(upper=q99).median(),
                "mean_capped_p99": valid["price"].clip(upper=q99).mean()
            }]).to_csv(TABLES / "price_outlier_sensitivity.csv", index=False)

            plt.figure(figsize=(9,5))
            sns.histplot(valid.loc[valid["price"] <= q99, "price"], bins=50, kde=True)
            plt.title("Advertised Nightly Price Distribution (up to P99)")
            plt.xlabel("Advertised nightly price (dataset currency)")
            plt.ylabel("Listings")
            plt.tight_layout(); plt.savefig(FIGURES / "price_distribution.png", dpi=150); plt.close()

            if "room_type" in valid:
                summary = valid.groupby("room_type", dropna=False)["price"].agg(
                    listing_count="count", median_price="median", mean_price="mean",
                    q1=lambda x:x.quantile(.25), q3=lambda x:x.quantile(.75))
                summary.sort_values("median_price", ascending=False).to_csv(TABLES / "price_by_room_type.csv")
                plot = valid.copy(); plot["price_display"] = plot["price"].clip(upper=q99)
                plt.figure(figsize=(10,6))
                sns.boxplot(data=plot, x="room_type", y="price_display")
                plt.title("Advertised Price by Room Type (capped at P99 for display)")
                plt.xlabel("Room type"); plt.ylabel("Nightly price (dataset currency)")
                plt.xticks(rotation=15); plt.tight_layout()
                plt.savefig(FIGURES / "price_by_room_type.png", dpi=150); plt.close()

            if "neighbourhood_group" in valid:
                summary = valid.groupby("neighbourhood_group", dropna=False)["price"].agg(
                    listing_count="count", median_price="median", mean_price="mean")
                summary.sort_values("listing_count", ascending=False).to_csv(TABLES / "price_by_neighbourhood_group.csv")
                plt.figure(figsize=(10,6))
                sns.barplot(data=summary.reset_index(), x="neighbourhood_group", y="listing_count")
                plt.title("Listings by Neighbourhood Group")
                plt.xlabel("Neighbourhood group"); plt.ylabel("Listings with valid prices")
                plt.xticks(rotation=20); plt.tight_layout()
                plt.savefig(FIGURES / "listings_by_neighbourhood_group.png", dpi=150); plt.close()

            if "number_of_reviews" in valid:
                reviews = pd.to_numeric(valid["number_of_reviews"], errors="coerce")
                ok = reviews.notna()
                rho = valid.loc[ok, "price"].corr(reviews.loc[ok], method="spearman")
                pd.DataFrame([{"n_listings":int(ok.sum()), "spearman_rho_price_vs_reviews":rho,
                    "note":"Association only; reviews are not bookings and exposure/listing age may confound results."}]).to_csv(TABLES / "numeric_correlations.csv", index=False)
                chart = valid.loc[ok & (valid["price"] <= q99)].copy()
                chart["number_of_reviews"] = reviews.loc[chart.index]
                plt.figure(figsize=(9,5))
                sns.scatterplot(data=chart, x="price", y="number_of_reviews", alpha=.35, s=20)
                plt.title("Advertised Price vs Number of Reviews (price capped at P99)")
                plt.xlabel("Advertised nightly price (dataset currency)"); plt.ylabel("Number of reviews")
                plt.tight_layout(); plt.savefig(FIGURES / "price_vs_reviews.png", dpi=150); plt.close()

    if "availability_365" in out:
        availability = pd.to_numeric(out["availability_365"], errors="coerce").dropna()
        plt.figure(figsize=(9,5)); sns.histplot(availability, bins=30)
        plt.title("Reported Availability Across Listings")
        plt.xlabel("Availability days in next 365 days"); plt.ylabel("Listings")
        plt.tight_layout(); plt.savefig(FIGURES / "availability_distribution.png", dpi=150); plt.close()
        if "room_type" in out:
            out.groupby("room_type", dropna=False)["availability_365"].agg(
                listing_count="count", median_availability="median", mean_availability="mean"
            ).to_csv(TABLES / "availability_by_room_type.csv")

    print("Done. Inspect outputs/tables and outputs/figures before writing findings.")
if __name__ == "__main__":
    main()
