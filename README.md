<div align="center">

# 🛍️ RetailPulse

### Customer Analytics & Demand Forecasting Platform

<p>
  <img alt="Python 3.13 local environment" src="https://img.shields.io/badge/Python-3.13-3776AB?style=for-the-badge&amp;logo=python&amp;logoColor=white" />
  <img alt="Streamlit dashboard" src="https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B?style=for-the-badge&amp;logo=streamlit&amp;logoColor=white" />
  <img alt="scikit-learn machine learning" src="https://img.shields.io/badge/scikit--learn-Machine_Learning-F7931E?style=for-the-badge" />
  <img alt="Prophet evaluated" src="https://img.shields.io/badge/Prophet-Evaluated-0F766E?style=for-the-badge" />
</p>

**📊 Customer Segmentation · 📈 Sales Forecasting · 🎯 Inactivity Prediction · 📦 Inventory Planning**

[**🚀 Explore Live Dashboard**](https://retailpulse-nandini57.streamlit.app/) · [**💻 View Repository**](https://github.com/rawlonandini57/RetailPulse)

</div>

---

## 🌐 Live Demo

- **Streamlit dashboard:** [retailpulse-nandini57.streamlit.app](https://retailpulse-nandini57.streamlit.app/)
- **GitHub repository:** [rawlonandini57/RetailPulse](https://github.com/rawlonandini57/RetailPulse)

## 📖 Project Overview

RetailPulse is a retail analytics portfolio project that turns historical transaction data into sales insights, customer segments, purchase-inactivity rankings, and inventory planning scenarios.

Using the **Online Retail II** dataset, the project combines data preparation, machine learning, forecast evaluation, and an interactive Streamlit dashboard.

The platform helps users explore:

- **Customer behavior:** understand purchase recency, frequency, and spend.
- **Sales patterns:** compare historical trends and forecast baselines.
- **Customer inactivity:** rank customers by their likelihood of making no purchase during a defined future period.
- **Inventory scenarios:** estimate replenishment quantities using explicit stock and lead-time assumptions.

> **Current scope:** A deployed dashboard with baseline analytics. Results refer to historical periods; advanced modeling and production MLOps remain planned. Business improvements have not yet been measured.

---

## ✨ Key Features

| Dashboard page | Capabilities |
|---|---|
| **Sales Overview** | Filter dates and explore gross merchandise purchase value, units sold, and invoice counts. |
| **Customer Segments** | Compare two provisional RFM-based groups and inspect customer records by segment. |
| **Demand Forecasting** | View a 30-day sales-unit forecast, earlier validation results, and downloadable forecasts. |
| **Churn Analysis** | Inspect historical 90-day inactivity rankings, model metrics, and the highest-risk 20% of customers. |
| **Inventory Planning** | Enter stock inputs, calculate replenishment scenarios, review product forecast validation, and download results. |

## 🏠 Home Dashboard

![RetailPulse Home Dashboard](screenshots/retailpulse_01_sales.jpg)

Explore historical gross merchandise purchase value, units sold, and daily sales trends using the date-range filter.

| Metric | Displayed value |
|---|---:|
| Date range | 1 December 2009 – 8 December 2011 |
| Gross merchandise value | £19,501,557 |
| Units sold | 11,127,909 |
| Days shown | 738 |

*Historical Online Retail II analysis. Monetary values are in GBP and represent gross merchandise purchases before returns.*

<!-- Keep screenshots/sales_overview.png in the repository root's screenshots folder so the relative image link renders on GitHub. -->

## 🛠️ Technology Stack

| Area | Tools used |
|---|---|
| Data preparation | Python, pandas, NumPy, openpyxl |
| Exploration | Jupyter Notebook, Matplotlib |
| Customer modeling | scikit-learn: K-Means and logistic regression |
| Forecast evaluation | Weekday-based baselines and Prophet |
| Dashboard | Streamlit |
| Source hosting and deployment | GitHub and Streamlit Community Cloud |

The dashboard loads prepared CSV outputs. It does **not** retrain models during page visits. `requirements.txt` covers dashboard dependencies; the notebook training environment requires separate dependencies.

## ⚙️ Run Locally

The original local setup used **Python 3.13**. Start from a copy of this repository containing the processed dashboard data.

### Windows Command Prompt

```bat
git clone https://github.com/rawlonandini57/RetailPulse.git
cd RetailPulse
py -3.13 -m venv .venv
.venv\Scripts\activate
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

Open **http://localhost:8501**. Keep the terminal running and press **Ctrl+C** to stop the app.

Theme settings belong in `.streamlit/config.toml`. If the browser retains a dark theme, select the custom theme in Streamlit's settings.

### Files required by the dashboard

| Path | Purpose |
|---|---|
| `app.py` | Streamlit application entry point |
| `requirements.txt` | Dashboard dependency versions |
| `.streamlit/config.toml` | Theme configuration |
| `data/processed/daily_sales.csv` | Historical daily sales |
| `data/processed/customer_segments.csv` | Customer segment assignments |
| `data/processed/segment_summary.csv` | Segment profiles |
| `data/processed/sales_forecast.csv` | Historical 30-day forecast |
| `data/processed/forecast_validation.csv` | Earlier-window forecasting metrics |
| `data/processed/churn_evaluation.csv` | Historical customer scores and outcomes |
| `data/processed/churn_metrics.csv` | Ranking evaluation metrics |
| `data/processed/inventory_scenarios.csv` | Product planning targets and stock inputs |
| `data/processed/product_forecast_validation.csv` | Product-level forecasting metrics |
| `data/processed/metadata.json` | Analysis dates, definitions, and assumptions |

Keep the `data/processed/` folder structure intact. The dashboard does not require the original Excel workbook to run, but reproducing model training does require the source data and analysis notebooks.

## 🏗️ Architecture

1. **Source data:** historical Excel transactions.
2. **Offline analysis:** cleaning, feature generation, segmentation, forecasting, inactivity modeling, and inventory scenarios.
3. **Prepared outputs:** nine CSV files plus metadata.
4. **Application:** Streamlit reads outputs and presents interactive views.
5. **Deployment:** GitHub provides application source to Streamlit Community Cloud.

There is no live ingestion service, online model training, or automated retraining in the current dashboard workflow.

## 📁 Project Structure

```text
RetailPulse-AI-Powered-Customer-Analytics-Demand-Forecasting-Platform/
├── .streamlit/
│   └── config.toml
├── data/
│   └── processed/
│       ├── churn_evaluation.csv
│       ├── churn_metrics.csv
│       ├── customer_segments.csv
│       ├── daily_sales.csv
│       ├── forecast_validation.csv
│       ├── inventory_scenarios.csv
│       ├── metadata.json
│       ├── product_forecast_validation.csv
│       ├── sales_forecast.csv
│       └── segment_summary.csv
├── notebooks/
│   └── 01_data_exploration.ipynb
├── screenshots/
│   └── retailpulse_01_sales.jpg
├── .gitignore
├── app.py
├── README.md
└── requirements.txt
```

| File or folder | Purpose |
|---|---|
| `.streamlit/config.toml` | Dashboard theme configuration |
| `data/processed/` | Prepared analytics outputs and metadata used by the dashboard |
| `notebooks/` | Project analysis notebook |
| `screenshots/` | Dashboard images used in the README |
| `app.py` | Streamlit dashboard entry point |
| `requirements.txt` | Dashboard Python dependencies |
| `.gitignore` | Rules for excluding local and temporary files |
| `README.md` | Project overview, results, and setup instructions |

The dashboard loads prepared outputs from `data/processed/` without retraining models during use.

## ✅ Dashboard Checks

Before sharing a new release, verify that all five pages load, date and segment filters update their outputs, downloads contain expected data, and inventory calculations respond correctly to both completed and cleared inputs.

## 🔗 Project Links

- **Live dashboard:** https://retailpulse-nandini57.streamlit.app/
- **Source repository:** https://github.com/rawlonandini57/RetailPulse

The analysis demonstrates a transparent baseline workflow. It should be presented with its historical scope, evaluation results, and assumptions intact.
