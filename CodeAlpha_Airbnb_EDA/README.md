# Airbnb Exploratory Data Analysis (EDA)

## Project Overview

This project analyzes Airbnb listing data to identify pricing patterns, neighborhood-level differences, room-type trends, listing availability, and data quality issues. It uses Python-based exploratory data analysis techniques to generate summary tables and visualizations.

## Project Objectives

- Explore Airbnb listing prices and their distribution.
- Compare prices across neighborhoods.
- Analyze room-type pricing and availability.
- Examine data quality and missing values.
- Investigate numerical correlations and price outliers.
- Generate visualizations and actionable business insights.

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook
- Visual Studio Code

## Project Structure

```text
CodeAlpha_Airbnb_EDA/
├── data/
│   ├── raw/
│   │   └── listings.csv.gz
│   └── processed/
├── notebooks/
├── outputs/
│   ├── figures/
│   └── tables/
├── reports/
│   ├── business_requirements.md
│   ├── data_source.md
│   └── findings_template.md
├── src/
├── README.md
└── requirements.txt
```

## Installation

### 1. Create and activate a virtual environment

Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 2. Install dependencies

```powershell
python -m pip install -r requirements.txt
```

## Running the Project

Open the project folder in Visual Studio Code.

Run the existing analysis script using its actual filename:

```powershell
python src/YOUR_SCRIPT_NAME.py
```

Replace `YOUR_SCRIPT_NAME.py` with the Python script that runs your analysis. If your workflow uses Jupyter Notebook, open the notebook in `notebooks/` and execute its cells in order.

## Outputs

The project generates analysis results in the following directories:

- `outputs/figures/` — charts and visualizations.
- `outputs/tables/` — CSV summaries and analytical results.

Generated tables cover neighborhood pricing, room-type pricing, availability, data quality, numeric correlations, and price outlier sensitivity.

## Expected Outcomes

The analysis helps identify pricing variation across neighborhoods, compare accommodation types, examine availability patterns, and understand potential data quality limitations.

## Limitations

The results depend on the supplied dataset and its quality. Observed price differences are descriptive and do not necessarily establish causation, booking demand, or profitability.

## Author
Vaibhav Dinesh Marathe
Data Analytics Intern, CodeAlpha
| LinkedIn [www.linkedin.com/in/vaibhavmarathe15] | GitHub [https://github.com/vmarathe1510-cpu/CodeAlpha_Airbnb_EDA]