# Airbnb Exploratory Data Analysis (EDA)

## 1. Project Overview

This project performs Exploratory Data Analysis (EDA) on Airbnb listing data to understand pricing patterns, room-type distributions, neighborhood differences, availability, and data quality. The analysis aims to extract meaningful insights that can support hosts, customers, and other stakeholders in understanding the short-term rental market.

## 2. Objectives

- Analyze Airbnb listing prices and their distribution.
- Compare median and average prices across neighborhoods.
- Examine pricing differences among room types.
- Analyze listing availability.
- Identify missing values, data quality issues, and potential price outliers.
- Generate tables and visualizations to communicate findings.

## 3. Tools and Technologies

- Python
- Pandas and NumPy
- Matplotlib and Seaborn
- Jupyter Notebook
- Visual Studio Code
- CSV and compressed CSV datasets

## 4. Methodology

### Data Collection
The project uses an Airbnb listings dataset stored in compressed CSV format.

### Data Cleaning
The analysis includes data profiling and quality summaries to examine missing values, data types, duplicates, and other potential inconsistencies. The exact cleaning operations should be documented according to the implemented scripts.

### Exploratory Data Analysis
The project examines price distributions, neighborhood-level pricing, room-type pricing, availability, numeric correlations, and sensitivity to price outliers.

### Visualization
Charts are generated to make pricing distributions and availability patterns easier to interpret.

## 5. Key Findings

### Neighborhood Pricing
The generated neighborhood summary indicates substantial variation in listing prices.

Among the neighborhoods visible in the output, Midtown has 1,421 listings, a median price of 473.84, and a mean price of 630.17. Greenwich Village has 79 listings, a median price of 449.00, and a mean price of 543.18.

In the displayed lowest-median-price results, Inwood has 65 listings, a median price of 61.12, and a mean price of 115.76. Fordham has 36 listings, a median price of 62.98, and a mean price of 81.85.

These results demonstrate differences in observed listing prices across neighborhoods. They describe the dataset and do not, by themselves, establish the causes of those differences.

### Room-Type Analysis
The project generates room-type pricing and availability summaries. These tables can be used to compare pricing patterns across accommodation types. Specific conclusions should be drawn from the completed output tables.

### Availability Analysis
The project includes availability summaries and an availability distribution chart. These outputs provide a basis for examining how listing availability varies across the dataset.

### Data Quality and Outliers
Data quality summaries, numeric correlations, and price outlier sensitivity tables are generated to support validation and interpretation of the analysis.

## 6. Business Insights

- Neighborhood-level price comparisons can help hosts understand the range of observed prices in their area.
- Median prices provide a useful comparison measure when average prices may be influenced by unusually expensive listings.
- Room-type comparisons can help identify differences in pricing across accommodation categories.
- Availability analysis can provide additional context when examining listing patterns.
- Data quality checks and outlier sensitivity analysis help assess the reliability of conclusions.

## 7. Limitations

- The findings depend on the coverage, quality, and time period of the supplied dataset.
- Observed price differences do not establish causation.
- Listing prices alone do not establish profitability or actual booking demand.
- Conclusions should account for missing data, unusual values, and differences in neighborhood sample sizes.

## 8. Conclusion

The Airbnb EDA project organizes listing data into meaningful summaries, visualizations, and neighborhood-level comparisons. It examines pricing, room types, availability, data quality, numeric relationships, and potential outliers. The resulting outputs provide a foundation for understanding variation in Airbnb listing prices and communicating data-driven observations.

## 9. Deliverables

- Data quality and column profile summaries
- Neighborhood price summaries
- Room-type pricing and availability tables
- Numeric correlation and outlier sensitivity tables
- Price distribution and availability visualizations
- Project documentation and reproducible analysis scripts
