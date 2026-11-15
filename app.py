import pandas as pd
import streamlit as st

st.set_page_config(page_title="Qahwa Corner Sales", page_icon="☕")
st.title("☕ Qahwa Corner — Sales Dashboard")
st.caption("Fictional Riyadh coffee chain · January–June 2026")

@st.cache_data
def load_data():
    return pd.read_csv("cafe_sales.csv", parse_dates=["date"])

df = load_data()

# 1) Branch selector
branches = ["All branches"] + sorted(df["branch"].unique())
choice = st.selectbox("Select a branch", branches)
data = df if choice == "All branches" else df[df["branch"] == choice]

# 2) Total-revenue metric
st.metric("Total revenue (SAR)", f"{data['total_sar'].sum():,.0f}")

# 3) Bar chart of revenue by product
st.subheader("Revenue by product")
by_product = data.groupby("product")["total_sar"].sum().sort_values(ascending=False)
st.bar_chart(by_product)
