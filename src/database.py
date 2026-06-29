import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
from src.config import DB_URL
from src.queries import INVOICES_QUERY, INVOICE_LINE_DETAIL_QUERY

@st.cache_data
def load_data():
    engine = create_engine(DB_URL)
    with engine.connect() as conn:
        invoices = pd.read_sql(INVOICES_QUERY, conn)
        invoice_line_detail = pd.read_sql(INVOICE_LINE_DETAIL_QUERY, conn)

    invoices["invoice_date"] = pd.to_datetime(invoices["invoice_date"])
    return invoices, invoice_line_detail