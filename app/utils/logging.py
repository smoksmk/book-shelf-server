import logging.config
import os


def create_logger(config):
    logger = logging.getLogger(config.APP_NAME)

    LOGGING_SETTINGS = {
        'version': 1,
        'formatters': {
            'default': {'format': ('%(levelname)s::%(asctime)s:%(name)s.'
                                   '%(funcName)s\n%(message)s\n'),
                        'datefmt': '%Y-%m-%d %H:%M:%S'}
        },
        'handlers': {
            'console': {
                'level': config.LOG_LEVEL,
                'class': 'logging.StreamHandler',
                'formatter': 'default',
                'stream': 'ext://sys.stdout'
            },
            'file': {
                'level': config.LOG_LEVEL,
                'class': 'logging.handlers.TimedRotatingFileHandler',
                'formatter': 'default',
                'filename': os.path.join('logs', 'app.log'),
                'when': 'midnight',
                'interval': 1,
                'backupCount': 10,
            },
        },
        'loggers': {
            config.APP_NAME: {
                'level': config.LOG_LEVEL,
                'handlers': (['console', 'file']),
            },
        },
        'disable_existing_loggers': False,
    }

    logging.config.dictConfig(LOGGING_SETTINGS)

    return logger

