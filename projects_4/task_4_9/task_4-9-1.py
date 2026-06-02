import psycopg2
connection = psycopg2.connect(
    host="5430",
    database="postgres_db",
    user="postgres_user",
    password="123456789"
)

# Используй это:
from sqlalchemy import create_engine

engine = create_engine("postgresql+psycopg2://postgres:ваш_пароль@localhost/school_db")

# И передавай engine в pd.read_sql:
df_years = pd.read_sql("SELECT ...", engine)