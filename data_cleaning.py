
import pandas as pd

file = "Brandon Nichols Sales and Revenue.xlsx"
df = pd.read_excel(file, sheet_name="train")

# Check original data
original_rows = len(df)
missing = df.isnull().sum().sum()
duplicates = df.duplicated().sum()

# Remove duplicate rows
df = df.drop_duplicates().copy()

# Clean extra spaces in text
for col in df.select_dtypes(include="object").columns:
    df[col] = df[col].apply(
        lambda x: x.strip() if isinstance(x, str) else x
    )

# Standardize date columns
df["Order Date"] = pd.to_datetime(
    df["Order Date"], errors="coerce"
)
df["Ship Date"] = pd.to_datetime(
    df["Ship Date"], errors="coerce"
)

# Flag dates for review
df["Check Ship Date"] = df["Ship Date"] < df["Order Date"]

# Create summary reports
category = df.groupby("Category")["Sales"].sum().reset_index()
region = df.groupby("Region")["Sales"].sum().reset_index()

df["Month"] = df["Order Date"].dt.to_period("M").astype(str)
monthly = df.groupby("Month")["Sales"].sum().reset_index()

quality = pd.DataFrame({
    "Metric": [
        "Original Rows",
        "Duplicate Rows Removed",
        "Remaining Rows",
        "Missing Values Before Cleaning",
        "Missing Postal Codes",
        "Shipping Dates to Review"
    ],
    "Value": [
        original_rows,
        duplicates,
        len(df),
        missing,
        df["Postal Code"].isna().sum(),
        df["Check Ship Date"].sum()
    ]
})

# Save everything into a new Excel workbook
with pd.ExcelWriter("Cleaned_Sales_Report.xlsx") as writer:
    df.to_excel(writer, sheet_name="Cleaned Data", index=False)
    quality.to_excel(writer, sheet_name="Data Quality", index=False)
    category.to_excel(writer, sheet_name="Category Report", index=False)
    region.to_excel(writer, sheet_name="Region Report", index=False)
    monthly.to_excel(writer, sheet_name="Monthly Report", index=False)

print("Data cleaning completed successfully!")
print(quality.to_string(index=False))
print("Report saved as Cleaned_Sales_Report.xlsx")
