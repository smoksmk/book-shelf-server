from flask import Flask
from flask_cors import CORS

from api.view.v1.view import bp
from app import config


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    CORS(app, resources={r"/*": {"origins": "*"}})
    app.register_blueprint(blueprint=bp, url_prefix='/v1')

    return app
