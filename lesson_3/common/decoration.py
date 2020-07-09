import sys
import yaml
import logging
import logging.config
from .variables import LOG_PATH_CONFIG_SERVER, LOG_PATH_CONFIG_CLIENT

if sys.argv[0].find('server') == -1:
    LOG_CONFIG = LOG_PATH_CONFIG_SERVER
    LOG_NAME = 'server'
else:
    LOG_CONFIG = LOG_PATH_CONFIG_CLIENT
    LOG_NAME = 'client'

with open(LOG_CONFIG, 'r') as f:
    config = yaml.safe_load(f.read())
    logging.config.dictConfig(config)
logger = logging.getLogger(LOG_NAME)


def log(func):
    """ Decorator function """

    def call(*args, **kwargs):
        logger.debug(f'Начало работы функции {func.__name__}, агрументы: {args}, {kwargs}. '
                     f'Вызвана из модуля {func.__module__}.')
        ret = func(*args, **kwargs)
        logger.debug(f'Функция {func.__name__} выполнена')
        return ret

    return call
