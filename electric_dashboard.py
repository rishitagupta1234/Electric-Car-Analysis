import streamlit as st

st.set_page_config(layout="wide")
st.title("🔋 Electric Car Dashboard Analysis")
st.markdown("This dashboard displays trends and insights about electric vehicles using Tableau.")

st.markdown("Click the button below to view the interactive Tableau dashboard:")

dashboard_url = "https://public.tableau.com/views/ElectricCarDashboardAnalysis2/ElectricCarAnalysis"
st.link_button("🔗 View Dashboard", dashboard_url)
