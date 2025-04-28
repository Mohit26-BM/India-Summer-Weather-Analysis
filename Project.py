import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

file_path = r"C:\Program Files\PostgreSQL\17\data\Indian Summers - Over the years.csv" # Change your path accordingly!
df = pd.read_csv(file_path)

# --- DATA EXPLORATION BEFORE CLEANING ---

# Display column names
print("\nColumn Names:")
print(df.columns.tolist())

# Quick overview of the dataset
print("\nDataFrame Info:")
df.info()

# Display missing values count and percentage
print("\nMissing Values Summary (Before Cleaning):")
missing_values = df.isnull().sum()
missing_percentage = (missing_values / len(df)) * 100
missing_summary = pd.DataFrame(
    {"Missing Values": missing_values, "Missing Percentage (%)": missing_percentage}
)
print(missing_summary)

# --- DATA CLEANING ---

# 1. Standardize column names
df.columns = df.columns.str.lower().str.replace(" ", "_")

# 2. Convert 'date' to datetime
df["date"] = pd.to_datetime(df["date"], errors="coerce")

# 3. Remove duplicate rows
df.drop_duplicates(inplace=True)

# 4. Handle missing values
# Drop rows where crucial fields are missing
df.dropna(subset=["date", "temp", "humidity", "tempmax", "tempmin"], inplace=True)

# 5.  Fill missing numeric columns with their mean
num_cols = df.select_dtypes(include="number").columns
df[num_cols] = df[num_cols].apply(lambda x: x.fillna(x.mean()))

# 6. Remove invalid entries
# Humidity must be between 0 and 100
df = df[(df["humidity"] >= 0) & (df["humidity"] <= 100)]

# Temperature ranges (basic check)
df = df[(df["temp"] > -50) & (df["temp"] < 60)]
df = df[(df["tempmax"] > -50) & (df["tempmax"] < 60)]
df = df[(df["tempmin"] > -50) & (df["tempmin"] < 60)]

# 7. Fix categorical columns
if "city" in df.columns:
    df["city"] = df["city"].str.title().str.strip()

# 8. Set 'date' as index
df.set_index("date", inplace=True)

# --- DATA EXPLORATION AFTER CLEANING ---

# Quick overview after cleaning
print("\nDataFrame Info After Cleaning:")
df.info()

# Display missing values count and percentage after cleaning
print("\nMissing Values Summary (After Cleaning):")
missing_values_after = df.isnull().sum()
missing_percentage_after = (missing_values_after / len(df)) * 100
missing_summary_after = pd.DataFrame(
    {
        "Missing Values": missing_values_after,
        "Missing Percentage (%)": missing_percentage_after,
    }
)
print(missing_summary_after)

# --- VISUALIZATIONS ---

# 1. Monthly Average Temperature Over Time
monthly_avg_temp = df["temp"].resample("M").mean()
plt.figure(figsize=(12, 6))
plt.plot(monthly_avg_temp.index, monthly_avg_temp.values, color="orange")
plt.title("Monthly Average Temperature Over Time")
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.tight_layout()
plt.show()

# 2. Temp Max vs Temp Min Line Plot
plt.figure(figsize=(12, 6))
plt.plot(df.index, df["tempmax"], label="Temp Max", alpha=0.7)
plt.plot(df.index, df["tempmin"], label="Temp Min", alpha=0.7)
plt.title("Daily Temp Max vs Temp Min")
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# 3. Humidity vs Temperature Scatter Plot
plt.figure(figsize=(10, 6))
plt.scatter(df["humidity"], df["temp"], alpha=0.4, c="green")
plt.title("Humidity vs Temperature")
plt.xlabel("Humidity (%)")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.tight_layout()
plt.show()

# 4. Average Temperature by City
if "city" in df.columns:
    city_avg_temp = df.groupby("city")["temp"].mean().sort_values(ascending=False)
    plt.figure(figsize=(12, 6))
    city_avg_temp.plot(kind="bar", color="skyblue")
    plt.title("Average Temperature by City")
    plt.xlabel("City")
    plt.ylabel("Average Temp (°C)")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()
