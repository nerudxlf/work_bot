from telebot import types

key_board_start = types.ReplyKeyboardMarkup(resize_keyboard=True)
key_board_start.add('Оставить заявку', 'Ифнормация обо мне')
key_board_start.row('Помощь', 'Контакты')