# Telecom Customer Churn Predictor

An ML-powered web app that predicts telecom customer churn risk and provides actionable retention recommendations.

## Live App
https://customer-churn-analysis-srv.streamlit.app/

## Problem
Telecom companies lose significant revenue to customer churn. This project identifies highest-risk customer segments and predicts individual churn probability using machine learning.

## Features
- ML churn predictor — enter customer details, get churn probability + retention recommendations
- Feature importance chart — understand what drives each prediction
- EDA notebooks — SQL + Python analysis of churn patterns

## Key Findings
1. Overall churn rate is **26.58%**
2. Month-to-month customers churn at **42.71%** vs **2.85%** for two-year contracts
3. Electronic check users churn at **45.29%** — 3x higher than automatic payment methods
4. **47.68%** of customers leave within first 12 months
5. Fiber optic customers churn at **41.89%** despite being premium service
6. Higher monthly charges correlate with higher churn (correlation: +0.19)

## Business Recommendations
1. Offer discounted annual contract upgrade to month-to-month customers at month 3
2. Incentivize automatic payment enrollment — reduces churn risk by 3x
3. Focus retention budget on first 12 months — nearly half of all churn happens here
4. Investigate fiber optic pricing and service quality
5. Flag senior citizens on month-to-month contracts as highest risk segment

## Tech Stack
Python, Pandas, scikit-learn, Streamlit, PostgreSQL, Seaborn

## Dataset
IBM Telco Customer Churn dataset via Kaggle — 7,032 customers, 21 features.
