APP_NAME = 'book-shelf'

PG_HOST = 'localhost'
PG_USERNAME = 'book_shelf'
PG_PASSWORD = 'book_shelf'
PG_SCHEMA = PG_USERNAME
PG_PORT = 5432

URL = f'postgresql://{PG_USERNAME}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/{PG_SCHEMA}'
