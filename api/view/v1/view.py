import flask


bp = flask.Blueprint('v1', __name__)


@bp.route('/book')
def books():
    return flask.jsonify('books')


@bp.route('/book/<id>')
def book(id):
    return flask.jsonify(f'book id: {id}')


@bp.route('/book', methods=['POST'])
def add_book():
    data = flask.request.json()
    return flask.jsonify(f'add book:')


@bp.route('/book/<id>', methods=['PATH'])
def update_book(id):
    data = flask.request.json()
    return flask.jsonify(f'update book: {id}')


@bp.route('/book/<id>', methods=['DELETE'])
def delete_book(id):
    return flask.jsonify(f'delete book: {id}')
