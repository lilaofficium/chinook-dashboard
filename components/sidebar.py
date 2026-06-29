import streamlit as st
import pandas as pd

def render_sidebar(invoices, invoice_line_detail):
    st.sidebar.header("Filters")

    country_options = ["All Countries"] + sorted(invoices["billing_country"].dropna().unique())
    selected_country = st.sidebar.selectbox("Country", options=country_options)

    data_min_date = invoices["invoice_date"].min().date()
    data_max_date = invoices["invoice_date"].max().date()

    date_range = st.sidebar.date_input(
        "Date Range",
        value=(data_min_date, data_max_date),
    )

    if len(date_range) != 2:
        st.info("Please select an end date to continue.")
        st.stop()

    if selected_country == "All Countries":
        country_mask = pd.Series([True] * len(invoices), index=invoices.index)
    else:
        country_mask = invoices["billing_country"] == selected_country

    filtered = invoices[
        country_mask
        & (invoices["invoice_date"].dt.date >= date_range[0])
        & (invoices["invoice_date"].dt.date <= date_range[1])
    ].copy()

    filtered_invoice_ids = filtered["invoice_id"].tolist()

    return filtered, filtered_invoice_ids