from app.utils import get_config

env = get_config()

APP_NAME = env['APP_NAME']

PG_HOST = env['PG_HOST']
PG_USERNAME = env['PG_USERNAME']
PG_PASSWORD = env['PG_PASSWORD']
PG_SCHEMA = env['PG_SCHEMA']
PG_PORT = env['PG_PORT']
LOG_LEVEL = env['LOG_LEVEL']

URL = f'postgresql://{PG_USERNAME}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/{PG_SCHEMA}'
