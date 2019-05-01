from flask import Flask
from flask_cors import CORS

from api.view.v1.view import bp
from app import config
from app.utils.error_heandlers import register_error_handler
from app.utils.logging import create_logger


def create_app():
    create_logger(config)
    app = Flask(__name__)
    app.config.from_object(config)
    register_error_handler(app)

    CORS(app, resources={r"*": {"origins": "*"}})
    app.register_blueprint(blueprint=bp, url_prefix='/v1')

    return app
