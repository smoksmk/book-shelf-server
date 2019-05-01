import flask

from api.models.models import Book
from app.exeptions import NotFoundError
from app.sqlalchemy import session_scope
from api.serializers import request

bp = flask.Blueprint('v1', __name__)


@bp.route('/books')
def books():
    with session_scope() as session:
        books = session.query(Book).all()
        return flask.jsonify(request.books_schema.dump(books).data)


@bp.route('/books/<int:id>')
def book(id):
    with session_scope() as session:
        try:
            book = session.query(Book).get(id)
        except Exception:
            raise NotFoundError('Book not found')
        return flask.jsonify(request.book_schema.dump(book).data)


@bp.route('/books', methods=['POST'])
def add_book():
    data = flask.request.json
    book = request.book_schema.load(data).data
    with session_scope() as session:
        model_book = Book(**book)
        session.add(model_book)
        session.flush()
        return flask.jsonify(request.book_schema.dump(model_book).data), 201


@bp.route('/books/<int:id>', methods=['PATCH'])
def update_book(id):
    data = request.book_schema.load(flask.request.json).data
    with session_scope() as session:
        try:
            model_book = session.query(Book).get(id)
        except Exception:
            raise NotFoundError("Book not found")
        model_book.name = data['name']
        model_book.description = data['description']
        model_book.image = data.get('image')
        model_book.url = data.get('url')
        session.add(model_book)
        session.flush()
        return flask.jsonify(request.book_schema.dump(model_book).data), 202


@bp.route('/books/<id>', methods=['DELETE'])
def delete_book(id):
    with session_scope() as session:
        try:
            model_book = session.query(Book).get(id)
        except Exception:
            raise NotFoundError("Book not found")
        session.delete(model_book)

    return '', 204


@bp.route('/ping')
def ping():
    return flask.jsonify('pong')
