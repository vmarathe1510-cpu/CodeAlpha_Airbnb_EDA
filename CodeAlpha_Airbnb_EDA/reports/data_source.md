# Data Source Documentation

## 1. Dataset Overview

The project uses an Airbnb listings dataset stored in compressed CSV format.

**File path:** `data/raw/listings.csv.gz`

**File format:** Gzipped CSV

**Purpose:** To perform exploratory data analysis on Airbnb listing prices, neighborhood patterns, room types, availability, reviews, and data quality, depending on the available columns.

## 2. Data Loading

The dataset is stored in the raw data directory. Python libraries such as Pandas can read compressed CSV files directly.

Example:

```python
import pandas as pd

df = pd.read_csv("data/raw/listings.csv.gz")
print(df.head())
print(df.shape)
print(df.columns.tolist())
```

Run this example from the project root directory. The dataset's actual source, geographic coverage, collection date, and licensing details should be recorded once verified from the original download or dataset documentation.

## 3. Data Preparation

The project should document the data preparation steps implemented in its existing scripts, including:

- Inspection of column names and data types.
- Assessment of missing values.
- Identification of duplicate records.
- Validation of price values.
- Treatment of invalid or extreme values, where applicable.
- Preparation of data for neighborhood and room-type comparisons.

Only transformations actually performed by the project scripts should be described as completed.

## 4. Generated Outputs

The project saves analytical results in the following directories:

- `outputs/tables/` — CSV summaries, including data quality, pricing, availability, correlations, and outlier sensitivity.
- `outputs/figures/` — PNG charts, including price distribution and availability distribution.

## 5. Data Quality Considerations

The analysis should account for missing information, inconsistent data types, unusual price values, and differences in sample sizes across neighborhoods. Summary statistics and outlier sensitivity analysis can help assess how these issues affect the findings.

## 6. Source and Attribution

The original dataset provider, source URL, access date, license, and any attribution requirements should be added after verifying the original download source.

The project should comply with the dataset provider's terms of use and applicable licensing conditions.
