from marshmallow import Schema, fields


class BookSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String()
    description = fields.String()
    image = fields.String()
    url = fields.String()


book_schema = BookSchema(strict=True)
books_schema = BookSchema(strict=True, many=True)
