import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

# ---------------------------
# Page Configuration
# ---------------------------
st.set_page_config(
    page_title="KPI-Driven Business Dashboard",
    layout="wide",
    page_icon="📊"
)

# ---------------------------
# Generate Sample Data
# ---------------------------
np.random.seed(42)

dates = pd.date_range(end=datetime.today(), periods=90)

data = pd.DataFrame({
    "date": dates,
    "revenue": np.random.randint(5000, 20000, size=len(dates)),
    "orders": np.random.randint(50, 200, size=len(dates)),
    "customers": np.random.randint(30, 150, size=len(dates)),
    "returns": np.random.randint(1, 20, size=len(dates))
})

data["conversion_rate"] = (data["orders"] / data["customers"]) * 100

# ---------------------------
# Sidebar Filters
# ---------------------------
st.sidebar.header("Filters")

start_date, end_date = st.sidebar.date_input(
    "Select Date Range",
    [data.date.min(), data.date.max()]
)

filtered_data = data[
    (data.date >= pd.to_datetime(start_date)) &
    (data.date <= pd.to_datetime(end_date))
]

# ---------------------------
# KPI Calculations
# ---------------------------
total_revenue = filtered_data["revenue"].sum()
total_orders = filtered_data["orders"].sum()
avg_conversion = filtered_data["conversion_rate"].mean()
return_rate = (filtered_data["returns"].sum() / filtered_data["orders"].sum()) * 100

# ---------------------------
# Dashboard Title
# ---------------------------
st.title("📊 KPI-Driven Business Dashboard")
st.caption("High-level KPIs with trend analysis and drill-down")

# ---------------------------
# KPI Cards
# ---------------------------
kpi1, kpi2, kpi3, kpi4 = st.columns(4)

kpi1.metric("Total Revenue", f"₹{total_revenue:,.0f}")
kpi2.metric("Total Orders", f"{total_orders:,}")
kpi3.metric("Avg Conversion Rate", f"{avg_conversion:.2f}%")
kpi4.metric("Return Rate", f"{return_rate:.2f}%")

st.divider()

# ---------------------------
# Trend Analysis
# ---------------------------
st.subheader("📈 Performance Trends")

trend1, trend2 = st.columns(2)

with trend1:
    st.line_chart(
        filtered_data.set_index("date")["revenue"]
    )

with trend2:
    st.line_chart(
        filtered_data.set_index("date")["orders"]
    )

# ---------------------------
# Distribution & Breakdown
# ---------------------------
st.subheader("📊 Distribution & Breakdown")

col1, col2 = st.columns(2)

with col1:
    weekly_revenue = filtered_data.copy()
    weekly_revenue["week"] = weekly_revenue.date.dt.isocalendar().week
    st.bar_chart(
        weekly_revenue.groupby("week")["revenue"].sum()
    )

with col2:
    st.area_chart(
        filtered_data.set_index("date")["conversion_rate"]
    )

# ---------------------------
# Data Table (Drill-down)
# ---------------------------
st.subheader("📋 Detailed Data View")
st.dataframe(filtered_data, use_container_width=True)

# ---------------------------
# Insights Section
# ---------------------------
st.subheader("🧠 Key Insights")

if avg_conversion > 60:
    st.success("Strong conversion rate — customer funnel is performing well.")
else:
    st.warning("Conversion rate can be improved with better targeting.")

if return_rate > 10:
    st.error("High return rate detected — review product quality or logistics.")
else:
    st.info("Return rate is within acceptable limits.")

# ---------------------------
# Footer
# ---------------------------
st.caption("Built with Streamlit • KPI-First Dashboard Design")
