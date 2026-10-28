# RetailPulse

Historical retail analytics using Online Retail II and Streamlit.

## Features
- Sales overview and date filtering
- Provisional RFM customer segmentation
- Historical 30-day sales-unit forecasting
- Historical 90-day customer inactivity evaluation
- Inventory scenarios and CSV downloads

## Setup
Open Command Prompt inside the RetailPulse folder.
Run these commands:

    py -3.13 -m venv .venv
    .venv\Scripts\activate
    python -m pip install -r requirements.txt
    python -m streamlit run app.py --theme.base=light --theme.primaryColor="#0f9488" --theme.backgroundColor="#f4f7fb" --theme.secondaryBackgroundColor="#ffffff" --theme.textColor="#16243a"

Open http://localhost:8501 and keep the terminal running.

## Required data
Keep all nine exported CSV files and metadata.json in data/processed/.
The dashboard reads these files without retraining models.
requirements.txt covers dashboard dependencies only.

## Current results
- Four-week weekday-average forecast: mean validation WAPE 35.16%.
- Churn logistic regression ROC-AUC: 0.731.
- Churn precision among highest-risk 20%: 0.632.
- Two customer clusters remain provisional.

## Limitations
- Historical prototype, not live or production-ready.
- Sales values are gross merchandise purchases before returns.
- Days without purchases are treated as zero sales.
- Forecasts cover December 2011 to January 2012, not current dates.
- Forecasts have no explicit Christmas or New Year adjustment.
- Churn means no purchase in the next 90 days, not permanent departure.
- Churn risk scores have not been calibrated.
- Inventory assumes 7-day lead time, 7-day review, and a 20% buffer.
- Stock inputs are unknown unless entered; recommendations are scenarios.
- The buffer is not statistically estimated safety stock.
- Accuracy targets and business impact have not been demonstrated.

## Pending work
- Final modeling, product forecast review, and temporal validation
- Reproducible training environment and automated pipelines
- MLflow, drift monitoring, and retraining
- Docker, CI/CD, public deployment, and Kubernetes configuration
- Full documentation, architecture diagram, and demo video
