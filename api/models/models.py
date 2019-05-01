import sqlalchemy as sa

from app import config
from app.sqlalchemy import Base


class Book(Base):
    __tablename__ = 'books'
    __table_args__ = {'schema': config.PG_SCHEMA}

    id = sa.Column('id', sa.BigInteger, primary_key=True, autoincrement=True)
    name = sa.Column('name', sa.String(255))
    description = sa.Column('description', sa.Text)
    image = sa.Column('image', sa.String(255))
    url = sa.Column('url', sa.String(255))

    def __init__(self, name=None, description=None, image=None, url=None):
        self.name = name
        self.description = description
        self.image = image
        self.url = url

    def __repr__(self):
        return f'{__class__.__name__}: name: {self.name}'
