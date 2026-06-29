# 🎵 Chinook Music Store Dashboard

An interactive sales analytics dashboard for the [Chinook](https://github.com/lerocha/chinook-database) music store database, built with **Streamlit** and **Python**.

---

## Overview

This dashboard connects to a PostgreSQL database (Chinook dataset) and provides an interactive interface to explore music store sales data — including revenue trends, top-performing artists, country-wise revenue breakdowns, and invoice-level details.

---

## Features

- **KPI Metrics** — at-a-glance summary of key sales figures
- **Top Artists Chart** — visualise the best-selling artists by revenue
- **Monthly Revenue Trend** — track revenue over time
- **Country Revenue Breakdown** — compare sales performance across countries
- **Invoice Table** — browse and filter detailed invoice records
- **Sidebar Filters** — dynamically filter all views by date, country, and more

---

## Project Structure

```
chinook-dashboard/
├── app.py                  # Main Streamlit entry point
├── requirements.txt        # Python dependencies
├── .env                    # Local environment variables (not committed)
├── .env.example            # Template for environment variables
├── components/
│   ├── sidebar.py          # Sidebar filter controls
│   ├── metrics.py          # KPI metric cards
│   ├── charts.py           # Chart visualisations
│   └── tables.py           # Invoice data table
└── src/
    ├── database.py         # Database connection and data loading
    └── config.py           # Configuration (reads DB_URL from .env)
```

---

## Prerequisites

- Python 3.8+
- A running PostgreSQL instance loaded with the [Chinook database](https://github.com/lerocha/chinook-database)

---

## Setup & Installation

**1. Clone the repository**

```bash
git clone https://github.com/lilaofficium/chinook-dashboard.git
cd chinook-dashboard
```

**2. Create and activate a virtual environment**

```bash
python -m venv .venv
source .venv/bin/activate        # On Windows: .venv\Scripts\activate
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

**4. Configure environment variables**

Copy the example file and fill in your database connection string:

```bash
cp .env.example .env
```

Then edit `.env`:

```env
DB_URL=postgresql://username:password@localhost:5432/chinook
```

**5. Run the app**

```bash
streamlit run app.py
```

The dashboard will open at `http://localhost:8501`.

---

## Dependencies

| Package | Purpose |
|---|---|
| `streamlit` | Web app framework |
| `pandas` | Data manipulation |
| `sqlalchemy` | Database ORM / connection |
| `psycopg2-binary` | PostgreSQL adapter |
| `matplotlib` | Plotting |
| `seaborn` | Statistical visualisations |
| `python-dotenv` | Load `.env` file |

---

## Environment Variables

| Variable | Description |
|---|---|
| `DB_URL` | PostgreSQL connection string (e.g. `postgresql://user:pass@host:port/dbname`) |

---

## License


This project is open source. The Chinook database is provided under the [MIT License](https://github.com/lerocha/chinook-database/blob/master/LICENSE.md).

---

## References

- [Chinook Database](https://github.com/lerocha/chinook-database) — original sample database by Luis Rocha (MIT License)
- [Northwind Database](https://github.com/microsoft/sql-server-samples/tree/master/samples/databases/northwind-pubs) — Microsoft's classic fictional food trading company dataset
- [Sakila Database](https://github.com/jOOQ/sakila) — MySQL's official DVD rental store sample (BSD License)
- [AdventureWorks](https://github.com/microsoft/sql-server-samples/tree/master/samples/databases/adventure-works) — Microsoft's fictional bicycle manufacturer dataset (68 tables)
- [WideWorldImporters](https://github.com/microsoft/sql-server-samples) — Microsoft's modern AdventureWorks successor with advanced SQL Server features
- [MySQL Employees Database](https://github.com/datacharmer/test_db) — HR benchmark dataset with ~300,000 employee records
- [World DB](https://dev.mysql.com/doc/world-setup/en/) — compact geographic/demographic dataset (countries, cities, languages)
- [Dell DVD Store (DellStore2)](https://linux.dell.com/dvdstore/) — open-source e-commerce simulation for benchmarking
- [Streamlit Documentation](https://docs.streamlit.io/) — web app framework used in this project
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/) — Python SQL toolkit and ORM
