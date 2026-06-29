import streamlit as st

def show_invoice_table(filtered):
    st.header("Raw Invoice Data")
    st.dataframe(filtered, use_container_width=True)