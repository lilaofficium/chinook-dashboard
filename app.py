import streamlit as st
from src.database import load_data
from src.config import DB_URL
from components.sidebar import render_sidebar
from components.metrics import show_metrics
from components.charts import top_artists_chart, monthly_trend_chart, country_revenue_chart
from components.tables import show_invoice_table

st.set_page_config(page_title="Chinook Music Dashboard", layout="wide")
st.title("Chinook Music Store Dashboard")

invoices, invoice_line_detail = load_data()

filtered, filtered_invoice_ids = render_sidebar(invoices, invoice_line_detail)

show_metrics(filtered)
top_artists_chart(invoice_line_detail, filtered_invoice_ids)
monthly_trend_chart(filtered)
country_revenue_chart(filtered)
show_invoice_table(filtered)