import psycopg2
from environs import Env

env = Env()
env.read_env()

DEBUG = env.bool("DEBUG")
PG_HOST = env("PG_HOST")
PG_USER = env("PG_USER")
PG_PASSWORD = env("PG_PASSWORD")
PG_DB = env("PG_DB")
PG_PORT = env.int("PG_PORT")

PG_URL = f"postgresql://{PG_USER}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/{PG_DB}"

print(f"Connecting to {PG_URL}...")

try:
    conn = psycopg2.connect(PG_URL)
    c = conn.cursor()
    c.execute("select 'hello, world!'")
    rows = c.fetchall()
    for r in rows:
        print(r)

except Exception as e:
    print("I am unable to connect to the database:")
    print(e)
