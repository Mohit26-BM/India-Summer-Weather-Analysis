# Summers in India: Analysis and Insights - Tableau Dashboard

This project presents an interactive Tableau dashboard analyzing summer weather patterns across major Indian cities from **April 1, 2012 to June 30, 2021**. It combines **PostgreSQL** for data processing with **Tableau** for visualization to uncover trends in temperature, humidity, and weather conditions.

---

## Project Overview

The goal of this project is to explore long-term summer climate trends in India and provide meaningful insights through data visualization. The dashboard enables users to compare cities, analyze seasonal variations, and understand weather patterns over time.

---

## Repository Structure

```

├── Dataset/
│   └── Indian Summers - Over the years.csv
│
├── Images/
│   ├── Dashboard/
│   │   ├── main_dashboard.png
│   │   ├── filter_usage.png
│   │   └── filter_use_ahmedabad.png
│   └── Queries/
│       ├── KPIs.png
│       └── charts.png
│
├── PostgreSQL/
│   ├── Main_Queries.sql
│   └── Summer_queries_1.sql
│
├── Workbook/
│   └── India_Summers.twb

```

---

## Dashboard Highlights

![Main Dashboard](Images/Dashboard/main_dashboard.png)

### Key Metrics
- **Total Days Analyzed:** 13,514  
- **Average Temperature:** 31.1°C  
- **Feels Like Temperature:** 33.7°C  
- **Average Humidity:** 54.7%  
- **Average Wind Speed:** 20.1 km/h  

### Visualizations
- Yearly average temperature trends (2012–2021)  
- City-wise humidity comparison  
- Temperature distribution using box plots  
- Monthly temperature averages  
- Weather condition distribution  

---

## Interactive Features

- **City Selection:** Analyze data across 15 major cities  
- **Weather Filters:** Filter by conditions such as Clear, Overcast, Rain, etc.  
- **Date Range Control:** Focus on specific periods between April 2012 and June 2021  

**Examples:**
- ![Using Filters](Images/Dashboard/filter_usage.png)  
- ![City Filter - Ahmedabad](Images/Dashboard/filter_use_ahmedabad.png)  

---

## Tools and Technologies

| Tool           | Role                              |
|----------------|-----------------------------------|
| Tableau        | Data visualization and dashboard design |
| PostgreSQL     | Data querying and transformation  |
| CSV Dataset    | Source data (cleaned and structured) |

---

## SQL Query Insights

- ![KPIs](Images/Queries/KPIs.png)  
- ![Charts](Images/Queries/charts.png)  

All SQL queries are available in the `PostgreSQL/` directory:
- `Main_Queries.sql` – Core query logic  
- `Summer_queries_1.sql` – Supporting queries for visualizations  

---

## Tableau Workbook

The Tableau workbook is located in the `Workbook/` directory:
- `India_Summers.twb` – Open using Tableau Desktop and connect to your PostgreSQL database  

---

## Use Cases

- Analyze long-term summer climate trends in India  
- Compare regional weather patterns across cities  
- Practice data visualization and SQL using a real-world dataset  
- Build portfolio-ready analytics projects  

---

## Getting Started

1. Clone the repository  
2. Import `Indian Summers - Over the years.csv` into PostgreSQL  
3. Execute SQL scripts from the `PostgreSQL/` folder  
4. Open `India_Summers.twb` in Tableau and connect to your database  

---

## Future Improvements

- Add more recent data for extended analysis  
- Incorporate additional weather parameters (e.g., rainfall, air quality)  
- Publish the dashboard to Tableau Public for wider accessibility  

---
