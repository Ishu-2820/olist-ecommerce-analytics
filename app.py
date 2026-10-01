import streamlit as st
import pandas as pd

st.set_page_config(page_title="Olist E-commerce Analytics", layout="wide")

k = pd.read_csv("kpis.csv").iloc[0]
monthly = pd.read_csv("monthly.csv")
cat = pd.read_csv("categories.csv")
ret = pd.read_csv("retention.csv").set_index("cohort")
bands = pd.read_csv("delivery_bands.csv").set_index("band")
states = pd.read_csv("state_late.csv").set_index("customer_state")
rep = pd.read_csv("repeat_by_late.csv").set_index("late").sort_index()

st.title("Olist E-commerce Analytics")
st.caption("Delivered orders, Jan 2017 - Aug 2018. Question: where is the business losing revenue and customers?")

c1, c2, c3, c4 = st.columns(4)
c1.metric("Revenue", f"{k['revenue']:,.0f}")
c2.metric("Unique customers", f"{int(k['customers']):,}")
c3.metric("Repeat customers", f"{k['repeat_pct']}%")
c4.metric("Late deliveries", f"{k['late_pct']}%")

st.subheader("1. Revenue plateaued after Black Friday 2017")
st.line_chart(monthly.set_index("month")["revenue"])
st.dataframe(cat, width="stretch")

st.subheader("2. 97% of customers buy only once")
st.write("Monthly retention % by first-order cohort (blank = not yet observed)")
st.dataframe(ret.style.background_gradient(cmap="Blues", axis=None).format("{:.2f}", na_rep=""))

st.subheader("3. Late deliveries wreck reviews")
a, b = st.columns(2)
a.write("Average review score by delivery timing")
a.bar_chart(bands["mean"])
b.dataframe(bands)

st.subheader("4. Where deliveries run late (% of orders)")
st.bar_chart(states["mean"])

st.subheader("5. Late first delivery and repeat purchase")
x, y = st.columns(2)
x.metric("Repeat rate, on-time first order", f"{rep['mean'].iloc[0]:.2f}%")
y.metric("Repeat rate, late first order", f"{rep['mean'].iloc[1]:.2f}%")

st.caption("Association, not proven cause. Window is 20 months, so recent customers have had little time to return.")
