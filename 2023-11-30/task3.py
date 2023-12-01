# Напишите код, который запускается из командной строки и получает на вход
# путь до директории на ПК.
# Соберите информацию о содержимом в виде объектов namedtuple.
# Каждый объект хранит:
# ○ имя файла без расширения или название каталога,
# ○ расширение, если это файл,
# ○ флаг каталога,
# ○ название родительского каталога.
# В процессе сбора сохраните данные в текстовый файл используя
# логирование.

import argparse
import json
import logging
import os
from collections import namedtuple

logger = logging.getLogger(__name__)
logging.basicConfig(
    filename=__name__ + '.txt',
    encoding='utf-8',
    filemode='w',
    format=f'%(asctime)s,%(name)s,%(funcName)s,%(levelname)s:\t%(message)s',
    level='DEBUG'
)

argparser = argparse.ArgumentParser()
argparser.add_argument('path', help='Type here path to discover')
ext_args = argparser.parse_args()
logger.debug(f'Args from command: {ext_args}')

path = os.path.abspath(ext_args.path)
logger.debug(f'Full path is {path}')

objects: list[namedtuple]


def listing(root):
    result = list()
    logger.debug(f'Root: {root}')
    for item in os.listdir(root):
        item_with_path = os.path.abspath(os.path.join(root, item))
        logger.debug(f'Item with path {item_with_path}')
        FSObject = namedtuple('FSObject', ['name', 'parrent', 'ext', 'isdir'])
        if os.path.isfile(item_with_path):
            item, ext = os.path.splitext(item)
            fsobject = FSObject(name=item, parrent=root, ext=ext, isdir=False)
            logger.debug(f'Adding file object {fsobject}')
            result.append(fsobject)
        else:
            fsobject = FSObject(name=item, parrent=root, ext=None, isdir=True)
            logger.debug(f'Adding dir object {fsobject}')
            result.append(fsobject)
            logger.debug(f'Calling self with path {item_with_path}')
            result.append(listing(item_with_path))
    logger.debug(f'Returning {result}')
    return result


if __name__ == '__main__':
    logger.debug(f'Calling listing with path: {path}')
    res = listing(path)
    for i in res:
        print(i)
