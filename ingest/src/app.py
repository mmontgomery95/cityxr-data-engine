from flask import Flask

import logging
import os.path
import psycopg2
import importlib.util
from environs import Env


logging.basicConfig(level=logging.DEBUG)

env = Env()
env.read_env()

DEBUG = env.bool("DEBUG")
PG_HOST = env("PG_HOST")
PG_USER = env("PG_USER")
PG_PASSWORD = env("PG_PASSWORD")
PG_DB = env("PG_DB")
PG_PORT = env.int("PG_PORT")

LISTEN_PORT = env.int("LISTEN_PORT")

PG_URL = f"postgresql://{PG_USER}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/{PG_DB}"


# try:
#     conn = psycopg2.connect(PG_URL)
#     c = conn.cursor()
#     c.execute("select 'hello, world!'")
#     rows = c.fetchall()
#     for r in rows:
#         print(r)

# except Exception as e:
#     print("I am unable to connect to the database:")
#     print(e)


app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World!"


def load_plugins():
    logging.info(f"Loading plugins...")
    script_path = os.path.abspath(__file__)
    script_dir = os.path.dirname(script_path)
    plugins_dir = os.path.join(script_dir, "user_plugins")
    for file in os.listdir(plugins_dir):
        plugin_path = os.path.join(plugins_dir, file)
        module_name = f"{file}"
        logging.info(f"\tloading plugin {module_name} from {plugin_path}...")
        spec = importlib.util.spec_from_file_location(
            f"plugin_{module_name}", plugin_path
        )
        plugin_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(plugin_module)
        plugin = plugin_module.Plugin()
        plugin.print()


if __name__ == "__main__":
    load_plugins()

    app.run(host="0.0.0.0", port=LISTEN_PORT)
