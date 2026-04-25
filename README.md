# Telecom Customer Churn Analysis

## Problem
Telecom companies lose significant revenue to customer churn. This project identifies which customer segments are highest risk and provides actionable retention recommendations using SQL, Python, and Power BI.

## Tools & Why
- **PostgreSQL** — chosen over MySQL/MariaDB for superior analytical functions and window functions. Industry standard for data roles.
- **Python + Pandas** — data cleaning and exploratory analysis
- **Power BI** — interactive dashboard for business stakeholders
- **Seaborn + Matplotlib** — statistical visualizations

## Key Findings
1. Overall churn rate is **26.58%**
2. Month-to-month customers churn at **42.71%** vs **2.85%** for two-year contracts
3. Electronic check users churn at **45.29%** — 3x higher than automatic payment methods
4. **47.68%** of customers leave within first 12 months
5. Fiber optic customers churn at **41.89%** despite being premium service
6. Higher monthly charges correlate with higher churn (correlation: +0.19)

## Business Recommendations
1. Offer discounted annual contract upgrade to month-to-month customers at month 3 — highest ROI intervention
2. Incentivize automatic payment enrollment — reduces churn risk by 3x
3. Focus retention budget on first 12 months — nearly half of all churn happens here
4. Investigate fiber optic pricing and service quality — premium customers should not churn at 42%
5. Flag senior citizens on month-to-month contracts as highest risk segment

## Project Structure

```
customer-churn-analysis/
├── data/
│   ├── raw/              # Original Kaggle dataset
│   └── cleaned/          # Cleaned data after processing
├── notebooks/
│   ├── data_cleaning.ipynb
│   ├── eda.ipynb
│   └── queries.sql       # PostgreSQL analysis queries
├── dashboard/
│   └── churn_dashboard.pbix
└── README.md
```

## Dataset
IBM Telco Customer Churn dataset via Kaggle — 7,032 customers, 21 features.
