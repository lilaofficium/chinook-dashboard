import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

def top_artists_chart(invoice_line_detail, filtered_invoice_ids):
    st.header("Top 10 Artists by Revenue")

    artist_revenue = (
        invoice_line_detail[
            invoice_line_detail["invoice_id"].isin(filtered_invoice_ids)
        ]
        .groupby("artist")["line_total"]
        .sum()
        .round(2)
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
        .rename(columns={"line_total": "revenue"})
    )

    if artist_revenue.empty:
        st.warning("No artist data for the selected filters.")
    else:
        fig1, ax1 = plt.subplots(figsize=(10, 6))
        sns.barplot(
            x="revenue", y="artist", data=artist_revenue,
            ax=ax1, palette="viridis",
        )
        ax1.set_xlabel("Revenue ($)")
        ax1.set_ylabel("Artist")
        ax1.set_title("Top 10 Artists by Revenue")

        for bar in ax1.patches:
            ax1.text(
                bar.get_width() + 0.5,
                bar.get_y() + bar.get_height() / 2,
                f"${bar.get_width():,.2f}",
                va="center", ha="left", fontsize=9,
            )

        plt.tight_layout()
        st.pyplot(fig1)
        plt.close(fig1)

    st.divider()


def monthly_trend_chart(filtered):
    st.header("Monthly Revenue Trend")

    filtered["month"] = filtered["invoice_date"].dt.strftime("%Y-%m")
    monthly = filtered.groupby("month")["total"].sum().reset_index()

    if monthly.empty:
        st.warning("No data for the selected filters.")
    else:
        fig2, ax2 = plt.subplots(figsize=(12, 5))
        sns.lineplot(
            x="month", y="total", data=monthly,
            marker="o", ax=ax2,
        )
        ax2.set_xlabel("Month")
        ax2.set_ylabel("Revenue ($)")
        ax2.set_title("Monthly Revenue Trend")
        ax2.grid(True, alpha=0.3)
        plt.xticks(rotation=45, ha="right")
        plt.tight_layout()
        st.pyplot(fig2)
        plt.close(fig2)

    st.divider()


def country_revenue_chart(filtered):
    st.header("Revenue by Country")

    country_rev = (
        filtered.groupby("billing_country")["total"]
        .sum()
        .sort_values(ascending=False)
        .reset_index()
        .rename(columns={"billing_country": "country", "total": "revenue"})
    )

    if country_rev.empty:
        st.warning("No country data for the selected filters.")
    else:
        fig3, ax3 = plt.subplots(figsize=(10, max(6, len(country_rev) * 0.4)))
        sns.barplot(
            x="revenue", y="country", data=country_rev,
            ax=ax3, palette="magma",
        )
        ax3.set_xlabel("Revenue ($)")
        ax3.set_ylabel("Country")
        ax3.set_title("Revenue by Country")

        for bar in ax3.patches:
            ax3.text(
                bar.get_width() + 0.5,
                bar.get_y() + bar.get_height() / 2,
                f"${bar.get_width():,.2f}",
                va="center", ha="left", fontsize=9,
            )

        plt.tight_layout()
        st.pyplot(fig3)
        plt.close(fig3)

    st.divider()