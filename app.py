from flask import Flask
from flask_login import LoginManager

from config import DevelopmentConfig

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.session_protection = "strong"
