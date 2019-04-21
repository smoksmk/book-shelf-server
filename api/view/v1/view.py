import flask


bp = flask.Blueprint('v1', __name__)


@bp.route('/hello')
def hello_world():
    return flask.jsonify('hello_world')
