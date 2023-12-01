# Задача 4
# Функция получает на вход текст вида: “1-й четверг ноября”, “3-
# я среда мая” и т.п.
# Преобразуйте его в дату в текущем году.
# Логируйте ошибки, если текст не соответсвует формату.
#
# Дорабатываем задачу 4.
# Добавьте возможность запуска из командной строки.
# При этом значение любого параметра можно опустить. В
# этом случае берётся первый в месяце день недели, текущий
# день недели и/или текущий месяц.
# *Научите функцию распознавать не только текстовое
# названия дня недели и месяца, но и числовые,
# т.е не мая, а 5.

import datetime
import argparse
import logging

# Logger initializer
logger = logging.getLogger(__name__)
logging.basicConfig(
    filename=__name__ + '.txt',
    encoding='utf-8',
    filemode='w',
    format=f'%(asctime)s,%(name)s,%(funcName)s,%(levelname)s:\t%(message)s',
    level='DEBUG'
)

# External command parsing
argparser = argparse.ArgumentParser()
argparser.add_argument('--nweek', help='Number of week (1-5)')
argparser.add_argument('--wday', help='Day of week (1-7)')
argparser.add_argument('--month', help='Month (1-12)')
argparser.add_argument('--text', help='Text like 1-я пятница ноября')
ext_args = argparser.parse_args()
logger.debug(f'Args from command: {ext_args}')


class Date:
    default_nweek = 1
    default_wday = 1
    default_month = datetime.datetime.now().month

    def __init__(self, nweek=None, wday=None, month=None, text=None):
        self.date = self.convert_args_to_date(nweek, wday, month, text)

    def convert_args_to_date(self, nweek: int, wday: int, month: int, text: str) -> datetime:
        year = datetime.datetime.now().year

        if text:
            text_nweek, text_wday, text_month = text.split()
            try:
                nweek = self._text_to_nweek(text_nweek)
                wday = self._text_to_wday(text_wday)
                month = self._text_to_month(text_month)
            except ValueError as e:
                logger.error(f'Value Error raised: {e}, setting default values')
                nweek = self.default_nweek
                wday = self.default_wday
                month = self.default_month
        else:
            try:
                logger.debug(f'Trying to convert to int {nweek=}, {wday=}, {month=}')
                nweek = int(nweek) - 1
                wday = int(wday) - 1
                month = int(month)
            except ValueError as e:
                logger.error(f'Value Error raised: {e}, setting default values')
                nweek = self.default_nweek
                wday = self.default_wday
                month = self.default_month

        basedate = datetime.date(year, month, 1) + datetime.timedelta(weeks=nweek)
        result = basedate + self._date_offset(basedate, wday)
        logger.debug(f'Returning datetime {result}')
        return result

    def _date_offset(self, _date: datetime.date, wday: int):
        result = _date
        timedelta = datetime.timedelta(days=0)
        for _ in range(7):
            if (result + timedelta).weekday() == wday:
                return timedelta
            timedelta += datetime.timedelta(days=1)

    def _text_to_wday(self, value: str, default: int = default_wday) -> int:
        logger.debug(f'Got {value} of type {type(value)}')
        weekdays = ('пон', 'вто', 'сре', 'чет', 'пят', 'суб', 'вос')
        try:
            result = weekdays.index(value[:3])
        except ValueError as e:
            logger.error(f'Value Error raised: {e}, setting default: {default}')
            result = default
        logger.debug(f'Returning {result}')
        return result

    def _text_to_month(self, value: str, default: int = default_month) -> int:
        if not default:
            default = datetime.datetime.now().month
        logger.debug(f'Got {value} of type {type(value)}')
        months = ('янв', 'фев', 'мар', 'апр', 'май', 'июн', 'июл', 'авг', 'сен', 'окт', 'ноя', 'дек')
        try:
            result = months.index(value[:3]) + 1
        except ValueError as e:
            logger.error(f'Value Error raised: {e}, setting default: {default}')
            result = default
        logger.debug(f'Returning {result}')
        return result

    def _text_to_nweek(self, value: str, default=default_nweek) -> int:
        logger.debug(f'Got {value} of type {type(value)}')
        result, _ = value.split('-')
        try:
            result = int(result) - 1
        except ValueError as e:
            logger.error(f'Value Error raised: {e}, setting default: {default}')
            result = default
        logger.debug(f'Returning {result}')
        return result


if __name__ == '__main__':
    date = Date(ext_args.nweek, ext_args.wday, ext_args.month, ext_args.text)
