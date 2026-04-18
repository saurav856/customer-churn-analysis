-- Overall Churn Rate
SELECT 
    COUNT(*) as total_customers,
    SUM(Churn) as churned,
    ROUND(AVG(Churn::numeric) * 100, 2) as churn_rate_percent
FROM telco;

-- Churn by Contract Type
SELECT 
    Contract,
    COUNT(*) as total,
    SUM(Churn) as churned,
    ROUND(AVG(Churn::numeric) * 100, 2) as churn_rate
FROM telco
GROUP BY Contract
ORDER BY churn_rate DESC;

-- Churn by Payment Method
SELECT 
    PaymentMethod,
    COUNT(*) as total,
    SUM(Churn) as churned,
    ROUND(AVG(Churn::numeric) * 100, 2) as churn_rate
FROM telco
GROUP BY PaymentMethod
ORDER BY churn_rate DESC;

-- Churn by Tenure Group
SELECT 
    CASE 
        WHEN tenure <= 12 THEN '0-12 months'
        WHEN tenure <= 24 THEN '13-24 months'
        WHEN tenure <= 48 THEN '25-48 months'
        ELSE '49+ months'
    END as tenure_group,
    COUNT(*) as total,
    SUM(Churn) as churned,
    ROUND(AVG(Churn::numeric) * 100, 2) as churn_rate
FROM telco
GROUP BY tenure_group
ORDER BY churn_rate DESC;

-- Churn by Internet Service
SELECT 
    InternetService,
    COUNT(*) as total,
    SUM(Churn) as churned,
    ROUND(AVG(Churn::numeric) * 100, 2) as churn_rate
FROM telco
GROUP BY InternetService
ORDER BY churn_rate DESC;