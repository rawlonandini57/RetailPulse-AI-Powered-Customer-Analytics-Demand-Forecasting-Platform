
from pathlib import Path
import json
import numpy as np
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="RetailPulse",
    page_icon="📊",
    layout="wide",
)


# RETAILPULSE_STYLE_START
st.markdown("""
<style>
.stApp {
    background: #f4f7fb;
    color: #16243a;
}

.block-container {
    max-width: 1450px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

[data-testid="stSidebar"] {
    background: #102438;
}
[data-testid="stSidebar"] h1,
[data-testid="stSidebar"] h2,
[data-testid="stSidebar"] p,
[data-testid="stSidebar"] label,
[data-testid="stSidebar"] span {
    color: #edf5fc !important;
}
[data-testid="stSidebar"] hr {
    border-color: #355069;
}
[data-testid="stSidebar"] [role="radiogroup"] {
    gap: 0.65rem;
}
[data-testid="stSidebar"] [role="radiogroup"] > label {
    background: #19364d;
    border: 1px solid #2b4b62;
    border-radius: 10px;
    padding: 12px 14px;
}
[data-testid="stSidebar"] [role="radiogroup"] > label:hover {
    background: #24516a;
}

[data-testid="stMetric"] {
    background: white;
    border: 1px solid #dce5ee;
    border-top: 4px solid #0f9488;
    border-radius: 14px;
    padding: 20px;
    box-shadow: 0 4px 14px rgba(16, 36, 56, 0.05);
}
[data-testid="stMetricValue"] {
    color: #102438;
    font-weight: 700;
}
[data-testid="stMetricLabel"] {
    color: #52657a;
}

.stButton > button,
.stDownloadButton > button {
    background: #0f766e;
    color: white;
    border: 0;
    border-radius: 9px;
    padding: 0.65rem 1rem;
}
.stButton > button:hover,
.stDownloadButton > button:hover {
    background: #115e59;
    color: white;
}
.stButton > button:focus-visible,
.stDownloadButton > button:focus-visible {
    outline: 3px solid #f59e0b;
    outline-offset: 3px;
}

.rp-hero {
    background: linear-gradient(115deg, #102438, #145b65);
    padding: 30px 34px;
    border-radius: 18px;
    margin-bottom: 24px;
}
.rp-eyebrow {
    color: #9de5dc;
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 2px;
    margin-bottom: 10px;
}
.rp-title {
    color: white;
    font-size: clamp(30px, 5vw, 44px);
    font-weight: 750;
    margin: 0;
    line-height: 1.2;
}
.rp-subtitle {
    color: #d6e8f0;
    font-size: 16px;
    margin-top: 12px;
}
.rp-badge {
    display: inline-block;
    background: #244b60;
    color: #e3f2f8;
    padding: 6px 12px;
    border-radius: 20px;
    font-size: 12px;
    margin-top: 16px;
}

/* RETAILPULSE_CONTRAST_FIX */
.rp-hero h1.rp-title {
    color: #ffffff !important;
    margin: 0 !important;
    padding: 0 !important;
}
.block-container {
    padding-top: 5rem !important;
}

</style>
""", unsafe_allow_html=True)
# RETAILPULSE_STYLE_END

DATA = Path(__file__).resolve().parent / "data" / "processed"

if not (DATA / "metadata.json").exists():
    st.error(f"Processed data not found in {DATA}")
    st.stop()

def load_csv(name):
    return pd.read_csv(
        DATA / name,
        dtype={"Customer ID": "string", "StockCode": "string"},
    )

metadata = json.loads(
    (DATA / "metadata.json").read_text(encoding="utf-8")
)


st.markdown("""
<div class="rp-hero">
    <div class="rp-eyebrow">RETAIL ANALYTICS</div>
    <h1 class="rp-title">RetailPulse</h1>
    <div class="rp-subtitle">
        Explore sales, understand customers, and plan inventory.
    </div>
    <div class="rp-badge">Online Retail II · Historical analysis · GBP</div>
</div>
""", unsafe_allow_html=True)

st.info(
    "Historical Online Retail II analysis. "
    "Sales are gross merchandise purchases before returns."
)

with st.sidebar:
    st.title("📊 RetailPulse")
    st.caption("Customer Analytics & Demand Forecasting")

    page = st.radio(
        "Navigation",
        [
            "Sales Overview",
            "Customer Segments",
            "Demand Forecasting",
            "Churn Analysis",
            "Inventory Planning",
        ],
    )

    st.divider()
    st.caption("Historical Online Retail II analysis · GBP")


if page == "Sales Overview":
    st.subheader("Sales overview")
    daily = load_csv("daily_sales.csv")
    daily["Date"] = pd.to_datetime(daily["Date"])

    start, end = st.slider(
        "Date range",
        min_value=daily["Date"].min().date(),
        max_value=daily["Date"].max().date(),
        value=(
            daily["Date"].min().date(),
            daily["Date"].max().date(),
        ),
    )

    selected = daily.loc[
        daily["Date"].dt.date.between(start, end)
    ]

    a, b, c = st.columns(3)
    a.metric("Gross merchandise value", f"£{selected['GrossSales'].sum():,.0f}")
    b.metric("Units sold", f"{selected['Units'].sum():,.0f}")
    c.metric("Days shown", len(selected))

    measure = st.selectbox("Chart measure", ["GrossSales", "Units", "Invoices"])
    st.line_chart(selected.set_index("Date")[[measure]])

elif page == "Customer Segments":
    st.subheader("Customer segments")
    st.caption(
        "Provisional two-cluster segmentation of customers purchasing "
        "within the final 365-day analysis window."
    )
    summary = load_csv("segment_summary.csv")
    customers = load_csv("customer_segments.csv")

    st.bar_chart(summary.set_index("Segment")[["Customers"]])
    st.dataframe(summary, hide_index=True)

    segment = st.selectbox(
        "View customers in segment",
        customers["Segment"].dropna().unique().tolist(),
    )
    st.dataframe(
        customers.loc[customers["Segment"].eq(segment)],
        hide_index=True,
    )

elif page == "Demand Forecasting":
    st.subheader("30-day historical forecast")
    st.caption(
        f"Model: {metadata['forecast_model']}. "
        "No explicit Christmas or New Year adjustment."
    )

    forecast = load_csv("sales_forecast.csv")
    forecast["Date"] = pd.to_datetime(forecast["Date"])

    st.line_chart(forecast.set_index("Date")[["ForecastUnits"]])
    st.dataframe(forecast, hide_index=True)

    st.write("Earlier validation windows")
    st.dataframe(load_csv("forecast_validation.csv"), hide_index=True)

    st.download_button(
        "Download forecast",
        forecast.to_csv(index=False).encode("utf-8"),
        file_name="sales_forecast.csv",
        mime="text/csv",
    )

elif page == "Churn Analysis":
    st.subheader("Historical churn evaluation")
    st.caption(
        "Predictions as of 1 September 2011. Target: no merchandise "
        "purchase in the next 90 days. Scores are not calibrated probabilities."
    )

    st.dataframe(load_csv("churn_metrics.csv"), hide_index=True)

    risks = load_csv("churn_evaluation.csv")
    top_only = st.checkbox("Show highest-risk 20% only", value=True)

    if top_only:
        risks = risks.loc[
            risks["Top20Percent"].astype(str).str.lower().eq("true")
        ]

    st.dataframe(
        risks.sort_values("ModelRiskScore", ascending=False),
        hide_index=True,
    )

elif page == "Inventory Planning":
    st.subheader("Inventory planning scenario")
    assumptions = metadata["inventory_assumptions"]
    st.caption(
        f"Assumed lead time: {assumptions['lead_time_days']} days. "
        f"Review interval: {assumptions['review_period_days']} days. "
        f"Illustrative buffer: {assumptions['buffer_fraction']:.0%}. "
        "Incoming orders are assumed to arrive within the planning period."
    )
    st.warning(
        "Enter stock inputs to calculate scenario orders. "
        "Blank inputs remain unknown. Edits are temporary unless downloaded."
    )

    inventory = load_csv("inventory_scenarios.csv")
    inputs = ["StockOnHand", "OnOrder", "Backorders"]

    # Hide previously calculated fields so edits cannot show stale results.
    base = inventory.drop(
        columns=["InventoryPosition", "SuggestedOrderUnits", "Status"],
        errors="ignore",
    )

    edited = st.data_editor(
        base,
        disabled=[column for column in base.columns if column not in inputs],
        column_config={
            column: st.column_config.NumberColumn(column, min_value=0.0)
            for column in inputs
        },
        hide_index=True,
        key="inventory_editor",
    )

    values = edited[inputs]
    valid = (
        values.notna().all(axis=1)
        & values.ge(0).all(axis=1)
        & np.isfinite(values).all(axis=1)
    )

    result = edited.copy()
    result["InventoryPosition"] = (
        result["StockOnHand"] + result["OnOrder"] - result["Backorders"]
    )
    result["SuggestedOrderUnits"] = np.nan
    result.loc[valid, "SuggestedOrderUnits"] = np.ceil(
        (
            result.loc[valid, "TargetInventoryPosition"]
            - result.loc[valid, "InventoryPosition"]
        ).clip(lower=0)
    )
    result["Status"] = np.where(
        valid, "Scenario calculated", "Missing or invalid stock inputs"
    )

    st.dataframe(
        result[["StockCode", "SuggestedOrderUnits", "Status"]],
        hide_index=True,
    )

    st.download_button(
        "Download inventory scenario",
        result.to_csv(index=False).encode("utf-8"),
        file_name="inventory_scenario.csv",
        mime="text/csv",
    )

    with st.expander("Product forecast validation"):
        st.dataframe(
            load_csv("product_forecast_validation.csv"),
            hide_index=True,
        )

with st.expander("Data limitations"):
    for limitation in metadata["limitations"]:
        st.write("- " + limitation)
