from flask import Flask
import mongoengine
from . import models

app = Flask(__name__)
mongoengine.connect("pulsarc-dev")


# Import done after app definition so that routes.py can import the app object
from . import routes
