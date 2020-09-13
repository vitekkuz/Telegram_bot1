import pytz as pytz

import categories
import exceptions

from typing import NamedTuple
import datetime


# Некое выполненное действие
class Action(NamedTuple):
    # кол-во повторений
    amount: int
    # категория действий
    category_name: str
    # время выполнения
    time: str


def parse_message(raw_message: str) -> Action:
    split_message = raw_message.strip().split(' ', 1)
    if len(split_message) != 2:
        raise exceptions.NonCorrectMessage(
            'Некорректное сообщение. Напишите сообщение в формате: \n'
            '50 отжимания'
        )

    if split_message[0].isdigit():
        amount = int(split_message[0].strip())
    else:
        raise exceptions.NonCorrectMessage(
            'Некорректное сообщение. Напишите сообщение в формате: \n'
            '50 отжимания'
        )
    category_name = split_message[1].strip()

    return Action(amount=amount,
                  category_name=category_name,
                  time=_get_now_datetime_formatted())


def _get_now_datetime_formatted() -> str:
    return _get_now_datetime().strftime('%Y-%m-%d %H:%M:%S')


def _get_now_datetime() -> datetime:
    tz = pytz.timezone("Europe/Moscow")
    now = datetime.datetime.now(tz)
    return now


def add_action(raw_message: str) -> Action:
    parsed_message = parse_message(raw_message)
    return Action(amount=parsed_message.amount,
                  category_name=parsed_message.category_name,
                  time=parsed_message.time)
