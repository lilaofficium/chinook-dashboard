import streamlit as st

def show_metrics(filtered):
    st.header("Key Metrics")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Total Revenue", f"${filtered['total'].sum():,.2f}")
    with col2:
        st.metric("Total Invoices", f"{len(filtered):,}")
    with col3:
        st.metric("Total Customers", f"{filtered['customer_id'].nunique():,}")

    st.divider()