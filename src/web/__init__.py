from flask import Flask
app = Flask(__name__)


# Import done after app definition so that routes.py can import the app object
from . import routes
