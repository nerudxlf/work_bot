from telebot import types


def keyboard_start():
    """
    function for add keyboard for bot
    :return: keyboard and it have 2 rows and 2 columns
    """
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row('Оставить заявку')
    keyboard.row('Ифнормация обо мне')
    keyboard.add('Помощь', 'Контакты')
    return keyboard


def keyboard_admin():
    """
    function add keyboard for admin
    :return: keyboard
    """
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add('Обновить информацию обо мне',
                 'Добавить контакты',
                 'Изменить контакты',
                 'Посмотреть заявки'
                 )
    return keyboard
