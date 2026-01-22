import streamlit as st
import pandas as pd
import numpy as np

st.title("🧠 ML Model Metrics Dashboard")

# ---------------------------
# Model Selection
# ---------------------------
models = ["Linear Regression", "Random Forest", "XGBoost"]
selected_model = st.selectbox("Select Model", models)

# ---------------------------
# Simulated Metrics (Demo)
# ---------------------------
metrics = {
    "Accuracy": np.random.uniform(0.85, 0.95),
    "Precision": np.random.uniform(0.80, 0.93),
    "Recall": np.random.uniform(0.78, 0.92),
    "F1 Score": np.random.uniform(0.80, 0.94),
    "RMSE": np.random.uniform(2.5, 6.0)
}

# ---------------------------
# KPI Cards
# ---------------------------
c1, c2, c3 = st.columns(3)

c1.metric("Accuracy", f"{metrics['Accuracy']:.2f}")
c2.metric("F1 Score", f"{metrics['F1 Score']:.2f}")
c3.metric("RMSE", f"{metrics['RMSE']:.2f}")

st.divider()

# ---------------------------
# Metrics Table
# ---------------------------
df_metrics = pd.DataFrame(
    {
        "Metric": metrics.keys(),
        "Value": [round(v, 3) for v in metrics.values()]
    }
)

st.subheader("📊 Detailed Metrics")
st.dataframe(df_metrics, use_container_width=True)

# ---------------------------
# Insight Section
# ---------------------------
if metrics["Accuracy"] > 0.90:
    st.success("Model accuracy is excellent.")
else:
    st.warning("Model accuracy can be improved.")

st.info("Use this dashboard to monitor model performance and drift.")
