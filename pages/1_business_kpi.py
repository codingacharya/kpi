import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

st.title("📊 Business KPI Dashboard")

# ---------------------------
# Role-Based Notice
# ---------------------------
if st.session_state.role == "Viewer":
    st.info("🔒 Viewer access: Read-only mode")

# ---------------------------
# Generate Sample Data
# ---------------------------
np.random.seed(42)
dates = pd.date_range(end=datetime.today(), periods=180)

df = pd.DataFrame({
    "date": dates,
    "revenue": np.random.randint(5000, 20000, len(dates)),
    "orders": np.random.randint(50, 200, len(dates)),
    "returns": np.random.randint(1, 20, len(dates)),
    "customers": np.random.randint(100, 300, len(dates))
})

df["conversion_rate"] = (df["orders"] / df["customers"]) * 100

# ---------------------------
# Time Granularity Toggle
# ---------------------------
granularity = st.radio(
    "📅 Time Granularity",
    ["Day", "Week", "Month"],
    horizontal=True
)

if granularity == "Week":
    df["period"] = df["date"].dt.isocalendar().week
elif granularity == "Month":
    df["period"] = df["date"].dt.month
else:
    df["period"] = df["date"]

grouped = df.groupby("period", as_index=False).sum(numeric_only=True)

# ---------------------------
# KPI Metrics
# ---------------------------
k1, k2, k3 = st.columns(3)

k1.metric("Total Revenue", f"₹{grouped['revenue'].sum():,.0f}")
k2.metric("Total Orders", int(grouped["orders"].sum()))
k3.metric("Avg Conversion Rate", f"{df['conversion_rate'].mean():.2f}%")

st.divider()

# ---------------------------
# Charts
# ---------------------------
c1, c2 = st.columns(2)

with c1:
    st.subheader("Revenue Trend")
    st.line_chart(grouped.set_index("period")["revenue"])

with c2:
    st.subheader("Orders Distribution")
    st.bar_chart(grouped.set_index("period")["orders"])

# ---------------------------
# Data Table (Drill-down)
# ---------------------------
st.subheader("📋 Detailed Data")
st.dataframe(df, use_container_width=True)

# ---------------------------
# Export CSV
# ---------------------------
st.download_button(
    label="📤 Download CSV",
    data=df.to_csv(index=False),
    file_name="business_kpi_data.csv",
    mime="text/csv"
)
