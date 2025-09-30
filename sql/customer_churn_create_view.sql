-- SQL example for customer_churn
CREATE OR REPLACE VIEW curated.customer_churn_view AS
SELECT * FROM parquet_scan('../lake/curated/customer_churn');
