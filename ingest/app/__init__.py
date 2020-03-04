from flask import Flask

app = Flask(__name__)

# keep this here, don't move it, don't delete it...
# it's a structural unused import
from app import views
