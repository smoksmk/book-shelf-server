import flask

from api.models.models import Book
from app.sqlalchemy import session_scope
from api.serializers import request

bp = flask.Blueprint('v1', __name__)


@bp.route('/book')
def books():
    with session_scope() as session:
        books = session.query(Book).all()
        return flask.jsonify(request.books_schema.dump(books).data)


@bp.route('/book/<int:id>')
def book(id):
    with session_scope() as session:
        book = session.query(Book).get(id)
        return flask.jsonify(request.book_schema.dump(book).data)


@bp.route('/book', methods=['POST'])
def add_book():
    data = flask.request.json
    book = request.book_schema.load(data).data
    with session_scope() as session:
        model_book = Book(**book)
        session.add(model_book)
        session.flush()
        return flask.jsonify(request.book_schema.dump(model_book).data), 201


@bp.route('/book/<id>', methods=['PATCH'])
def update_book(id):
    data = request.book_schema.load(flask.request.json).data
    with session_scope() as session:
        model_book = session.query(Book).get(id)
        model_book.name = data['name']
        model_book.description = data['description']
        model_book.image = data['image']
        model_book.url = data['url']
        session.add(model_book)
        session.flush()
        return flask.jsonify(request.book_schema.dump(model_book).data), 202


@bp.route('/book/<id>', methods=['DELETE'])
def delete_book(id):
    with session_scope() as session:
        model_book = session.query(Book).get(id)
        session.delete(model_book)

    return '', 204
