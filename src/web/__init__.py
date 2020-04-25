from flask import Flask
from flask_login import LoginManager

app = Flask(__name__)
loginMan = LoginManager()
loginMan.init_app(app)
loginMan.login_view = "login"
app.secret_key = "Epic Awesome Secret Key That Should Not Be Here In The Open Code"  # TODO: MOVE THIS TO A DATABASE


# Import done after app definition so that routes.py can import the app object
from . import routes, authRoutes
