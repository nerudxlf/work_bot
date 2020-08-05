import telebot
import config
import keybord
import db_worker

bot = telebot.TeleBot(config.TOKEN)


def main():
    @bot.message_handler(commands=['start'])
    def start_msg(message):
        """COMMAND START"""
        bot.send_message(message.chat.id, 'Приветствую Вас', reply_markup=keybord.keyboard_start())
        db_worker.adding_new_user(message, config.Query.insert_user.value, config.Query.select_user.value)
        db_worker.update_state(message.chat.id, config.Query.update_state.value, config.StateUser.S_START.value)

    @bot.message_handler(commands=['admin'])
    def check_admin_msg(message):
        if str(message.chat.id) == config.ID_ADMIN:
            bot.send_message(message.chat.id, 'Привет админ', reply_markup=keybord.keyboard_admin())
            db_worker.update_state(message.chat.id, config.Query.update_state.value, config.StateAdmin.S_START.value)
        else:
            bot.send_message(message.chat.id, 'Вы не админ')

    @bot.message_handler(content_types=['text'])
    def send_msg(message):
        """BOT MENU"""
        if message.text.lower() == 'информация обо мне':
            bot.send_message(message.chat.id, 'Сообщение')
        elif message.text.lower() == 'оставить заявку':
            bot.send_message(message.chat.id, 'Оставить заявку')
        elif message.text.lower() == 'помощь':
            bot.send_message(message.chat.id, 'Помощь')
        elif message.text.lower() == 'контакты':
            bot.send_message(message.chat.id, 'Контакты')

    bot.polling()


if __name__ == '__main__':
    main()