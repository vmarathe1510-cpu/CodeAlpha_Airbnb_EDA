# Business Requirements — Airbnb Exploratory Data Analysis

## 1. Business Problem

Airbnb listing data contains information about nightly prices, room types, neighborhoods, reviews, and availability. Analyzing these attributes can help stakeholders understand listing-price variation and identify useful market patterns.

## 2. Project Goal

The goal of this project is to analyze Airbnb listing data using Exploratory Data Analysis (EDA) and present the findings through summary tables, statistical analysis, and visualizations.

## 3. Business Objectives

- Understand the distribution of advertised nightly prices.
- Compare median and mean prices across neighborhoods.
- Examine price differences by room type.
- Analyze listing availability patterns.
- Explore the relationship between prices and review-related variables where available.
- Identify data quality issues and assess the impact of extreme prices.
- Present findings in a clear, reproducible format.

## 4. Stakeholders

- **Airbnb hosts:** To understand observed prices in different neighborhoods.
- **Guests:** To explore price variation across locations and accommodation types.
- **Market analysts:** To study listing distributions and neighborhood-level patterns.
- **Project reviewers:** To evaluate the data analysis process and its results.

## 5. Data Requirements

The project uses the Airbnb listings dataset stored at `data/raw/listings.csv.gz`.

Relevant fields depend on the columns available in the dataset and may include:

- Listing price
- Neighborhood
- Room type
- Availability
- Review-related attributes
- Other numeric listing characteristics

The data must be profiled and checked for missing values, invalid entries, duplicates, and inconsistent data types before interpreting the results.

## 6. Analytical Requirements

The project should produce:

1. A data quality summary and column profile.
2. A summary of listing prices.
3. Neighborhood-level price comparisons.
4. Room-type pricing summaries.
5. Availability analysis.
6. Numeric correlation analysis.
7. Price outlier sensitivity analysis.
8. Clear visualizations of the major findings.

## 7. Expected Deliverables

- Reproducible Python scripts or notebooks.
- Cleaned or processed data, where applicable.
- CSV summary tables in `outputs/tables/`.
- PNG visualizations in `outputs/figures/`.
- Project documentation and a final findings report.

## 8. Success Criteria

The project will be considered ready for review when:

- The analysis runs without errors.
- Generated tables and charts are saved in the expected locations.
- Reported findings agree with the generated outputs.
- Data cleaning and analytical methods are documented.
- The README provides clear setup and execution instructions.
- Limitations and assumptions are stated honestly.

## 9. Limitations

This analysis describes patterns in the available dataset. It does not independently establish causation, actual booking demand, profitability, or the ideal price for an individual listing.
