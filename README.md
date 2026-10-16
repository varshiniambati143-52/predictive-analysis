# Data Cleaning & Reporting Automation

## Project Overview

This project focuses on automating data cleaning and reporting workflows using Python and Power BI. It uses a sales and revenue dataset to identify data quality issues, clean records, and generate summarized reports for business analysis.

## Objectives

- Automate repetitive data cleaning tasks.
- Identify and handle duplicate records and missing values.
- Standardize text and date formats.
- Generate sales summaries by category, region, and month.
- Visualize sales performance using Power BI dashboards.
- Improve reporting efficiency and data quality.

## Tools & Technologies

- **Python** – Data processing and automation
- **Pandas** – Data cleaning and analysis
- **OpenPyXL** – Excel file processing
- **Microsoft Excel** – Data storage and report generation
- **Microsoft Power BI** – Data visualization and dashboard creation
- **Visual Studio Code** – Python development environment
- **GitHub** – Version control and project hosting

## Dataset

The project uses a sales and revenue dataset containing order information, customer details, product categories, regional information, shipping dates, and sales values.

## Data Cleaning Process

1. Import the Excel dataset using Pandas.
2. Check for missing values and duplicate records.
3. Remove exact duplicate rows.
4. Remove unnecessary spaces from text fields.
5. Standardize date columns.
6. Identify shipping dates that require verification.
7. Generate data quality statistics.

## Reporting and Visualization

The project generates an Excel report containing the following sheets:

- **Cleaned Data** – Processed sales records.
- **Data Quality** – Summary of missing values, duplicates, and dates requiring review.
- **Category Report** – Total sales by product category.
- **Region Report** – Total sales by region.
- **Monthly Report** – Monthly sales summaries.

Power BI is used to create visualizations, including:

- Sales by Category (Column Chart)
- Sales by Region (Bar Chart)
- Monthly Sales Trend (Line Chart)

## Project Structure

```text
data-cleaning-reporting-automation/
│
├── data_cleaning.py
├── README.md
└── .gitignore
```

The generated Excel reports and source dataset are kept locally and are not included in the public repository.

## How to Run the Project

### 1. Install Python

Download Python from https://www.python.org/downloads/

### 2. Install the required libraries

Open the terminal and run:

```bash
python -m pip install pandas openpyxl
```

### 3. Prepare the dataset

Place the Excel dataset in the same folder as `data_cleaning.py`.

The input workbook should contain a worksheet named `train` and the required column names.

### 4. Run the Python script

```bash
python data_cleaning.py
```

### 5. View the output

After successful execution, the script generates:

```text
Cleaned_Sales_Report.xlsx
```

Open this file in Microsoft Excel to view the cleaned data and summary reports.

### 6. Create the Power BI dashboard

Import `Cleaned_Sales_Report.xlsx` into Power BI Desktop and create the required charts.

## Expected Outcomes

- Reduced manual data cleaning effort.
- Improved consistency of sales records.
- Identification of data quality issues.
- Automated generation of summary reports.
- Clear visual insights into sales performance.

## Conclusion

This project demonstrates how Python can automate data preprocessing and report generation. By combining Pandas, Excel, and Power BI, the workflow supports efficient reporting and helps transform raw sales data into meaningful business insights.

## Author

**Varshini Ambati**

GitHub: https://github.com/varshiniambati143-52

## Project Type

Internship Project – Data Cleaning & Reporting Automation
