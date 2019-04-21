from flask import jsonify
from marshmallow.exceptions import ValidationError

from app.exeptions import InternalError, NotFoundError


def get_error_response(message, detail=None):
    return jsonify({
        'message': message,
        'detail': detail
    })


def register_error_heandler(app):
    @app.errorhandler(Exception)
    def exception(e):
        return get_error_response(message='Internal Error'), 500

    @app.errorhandler(InternalError)
    def internal_error(e):
        return get_error_response(e.message, e.detail), e.code

    @app.errorhandler(NotFoundError)
    def not_found_error(e):
        return get_error_response(e.message, e.detail), e.code

    @app.errorhandler(ValidationError)
    def validation_error(e):
        return get_error_response('Validate error', detail=e.message), 400

