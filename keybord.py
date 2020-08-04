from telebot import types


def key_board():
    key_board_start = types.ReplyKeyboardMarkup(resize_keyboard=True)
    key_board_start.row('Оставить заявку')
    key_board_start.row('Ифнормация обо мне')
    key_board_start.add('Помощь', 'Контакты')
    return key_board_start
