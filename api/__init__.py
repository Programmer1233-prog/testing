from flask import Flask
from .routes.face_detection import api
#local imports
from config import config

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config.get(config_name, "development"))

    api.init_app(app)

    return app