import os
from dotenv import load_dotenv

load_dotenv()

USER     = os.getenv("NEON_USER")
PASSWORD = os.getenv("NEON_PASSWORD")
HOST     = os.getenv("NEON_HOST")
PORT     = os.getenv("NEON_PORT")
DBNAME   = os.getenv("NEON_DBNAME")

DB_URL = (
    f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DBNAME}"
    f"?sslmode=require"
)