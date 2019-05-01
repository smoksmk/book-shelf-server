import logging

from flask import jsonify, request
from marshmallow.exceptions import ValidationError
from sqlalchemy.exc import DatabaseError
from .exeptions import InternalError

from app import config


logger = logging.getLogger(config.APP_NAME)


def get_error_response(code, message, detail):
    return jsonify({
        'error': {
            'code': code,
            'message': message,
            'detail': detail
        }
    }), code


def register_error_handler(app):
    @app.errorhandler(400)
    def bad_request(e):
        return get_error_response(
            400,
            'the browser (or proxy) sent a request that this server could not understand',
            'bad request'
        )

    @app.errorhandler(401)
    def unauthorized(e):
        return get_error_response(401, 'missing or bad authentication', 'unauthorized')

    @app.errorhandler(404)
    def not_found(e):
        return get_error_response(404, 'invalid resource URI', 'not found')

    @app.errorhandler(405)
    def method_not_supported(e):
        return get_error_response(405, 'the request method is not allowed', 'method not supported')

    @app.errorhandler(500)
    def internal_server_error(e):
        e.args = f'{e.args} request_url: {request.url} request_data: {request.data}'
        logger.exception(e)
        return get_error_response(500, 'sorry about inconvenience', 'internal server error')

    @app.errorhandler(ValidationError)
    def validation_error(e):
        return get_error_response(400, 'Validation Error', e.message)

    @app.errorhandler(InternalError)
    def internal_server_error(e):
        e.args = f'{e.args} request_url: {request.url} request_data: {request.data}'
        logger.exception(e)
        return get_error_response(500, 'sorry about inconvenience', 'internal server error')

    @app.errorhandler(DatabaseError)
    def database_error(e):
        logger.exception(e)
        return get_error_response(500, 'Internal Error', 'Data base error')


