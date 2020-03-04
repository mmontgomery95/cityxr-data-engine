from plugin_manager import PluginManager
from app import app
from config import LISTEN_PORT

if __name__ == "__main__":
    pm = PluginManager()
    pm.load_plugins()
    app.run(host="0.0.0.0", port=LISTEN_PORT)
