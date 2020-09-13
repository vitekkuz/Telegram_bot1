import telebot
from settings import *
import datetime

from TV_guide import TVguide
import actions
import exceptions

bot = telebot.TeleBot(TOKEN)


def auth(func):
    def wrapper(message):
        if str(message.from_user.id) != MY_ID:
            return bot.send_message(message.chat.id, "Access Denied. id = " + str(message.from_user.id))
        return func(message)

    return wrapper


@bot.message_handler(commands=['start', 'help'])
@auth
def help_message(message):
    bot.send_message(
        message.chat.id,
        'Бот для учета потраченного времени \n\n' +
        '1) Добавить действие: отжамания 50 \n' +
        '2) Сегодняшняя статистика: /today \n' +
        '3) Статистика за месяц: /month\n' +
        '4) Список возможных действий: /categories \n'
    )


@bot.message_handler(commands=['tv_guide'])
@auth
def help_message(message):
    tv_guide = TVguide()
    bot.send_message(
        message.chat.id, tv_guide.parse()
    )


@bot.message_handler(content_types=['text'])
# метод для получения текстовых сообщений
@auth
def add_action(message):
    try:
        action = actions.add_action(message.text)
    except exceptions.NonCorrectMessage as e:
        bot.send_message(message.chat.id, str(e))
        return
    answer_message = (
            f'Добавлено действие: {action.category_name} - {action.amount} раз \n'
            f'Время: ' + action.time
    )
    bot.send_message(message.chat.id, answer_message)


if __name__ == '__main__':
    print('Bot in work....' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    bot.polling(none_stop=True, interval=0)
