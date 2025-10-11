# Customer Churn
This project is converted to be Fabric + Power BI ready.

## Contents
- `data/` sample CSV for local testing
- `notebooks/01_ingest_transform.ipynb` — PySpark notebook to ingest CSV and write parquet to `../lake/curated/customer_churn`
- `notebooks/02_analysis_or_model.ipynb` — analysis / model notebook
- `sql/` SQL scripts to create views over curated data
- `powerbi/` Power Query M and instructions to build the report
- `lake/` (not included) — intended target for curated parquet in Fabric Lakehouse

## How to use in Fabric
1. Upload the `data/` files to your ADLS Gen2 or Lakehouse `lake/raw/customer_churn/`.
2. Open the notebooks in Fabric, run `01_ingest_transform` to produce parquet under `lake/curated/customer_churn`.
3. Use Power BI to connect to the curated location and create a report. See `powerbi/report_instructions.md`.

<img width="1274" height="609" alt="image" src="https://github.com/user-attachments/assets/b30b57ca-98a3-44e2-ac20-1f43b0816855" />
