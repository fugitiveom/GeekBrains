# Возьмите любые 1-3 задачи из прошлых домашних заданий.
# Добавьте к ним логирование ошибок и полезной
# информации. Также реализуйте возможность запуска из
# командной строки с передачей параметров.

import logging
import argparse

argparser = argparse.ArgumentParser()
argparser.add_argument('--key', metavar='k')
argparser.add_argument('--value', metavar='v')
ext_args = argparser.parse_args()

logging.basicConfig(
    filemode='w',
    filename=__name__,
    level='DEBUG',
    format='%(asctime)s %(levelname)s:\t%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)


def return_args(**kwargs):
    result = {}
    logger.debug(f'args income: {kwargs}')
    for key, value in kwargs.items():
        try:
            logger.debug(f'Trying to hash object of type: {type(value)}')
            hash(value)
            result[value] = key
        except TypeError as e:
            logger.error(f'Got TypeError {e}')
            result[str(value)] = key
    logger.debug(f'Returning result: {result}')
    return result


if ext_args.key and ext_args.value:
    return_args(**{ext_args.key: ext_args.value})
else:
    return_args(name="Vasya", age=30, custom_object={1, 2, 3})
