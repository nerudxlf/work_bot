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
            db_worker.update_state(message.chat.id, config.StateAdmin.S_START.value)
        else:
            bot.send_message(message.chat.id, 'Вы не админ')

    @bot.message_handler(func=lambda message: db_worker.get_current_state(
        message.chat.id) == config.StateUser.S_NAME_REQUEST.value)
    def request_name(message):
        db_worker.add_new_request_name(message)
        bot.send_message(message.chat.id, 'Опишите задание как можно подробнее')
        db_worker.update_state(message.chat.id, config.Query.update_state.value, config.StateUser.S_INFO_REQUEST.value)

    @bot.message_handler(func=lambda message: db_worker.get_current_state(
        message.chat.id) == config.StateUser.S_INFO_REQUEST.value)
    def request_info(message):
        db_worker.update_info_request(message, config.Query.update_info_request.value)
        bot.send_message(message.chat.id, 'Введите возможный бюджет\nПример: 4000 руб.')
        db_worker.update_state(message.chat.id, config.Query.update_state.value, config.StateUser.S_PRICE.value)

    @bot.message_handler(func=lambda message: db_worker.get_current_state(
        message.chat.id) == config.StateUser.S_PRICE.value)
    def request_price(message):
        msg_reply = '\n'.join(config.contacts_arr)
        db_worker.update_info_request(message, config.Query.update_price_request.value)
        bot.send_message(message.chat.id, 'В течении суток вам ответят. Откройте личные сообщения\n\nВы можете сами '
                                          'связаться со мной\n' + msg_reply)
        db_worker.update_state(message.chat.id, config.Query.update_state.value, config.StateUser.S_START.value)

    @bot.message_handler(content_types=['text'])
    def bot_menu(message):
        """BOT MENU"""
        if message.text.lower() == 'информация обо мне':
            bot.send_message(message.chat.id, 'Сообщение')
        elif message.text.lower() == 'оставить заявку':
            bot.send_message(message.chat.id, 'Введите название услуги\n(Чат-бот, верстка, доработка)')
            db_worker.update_state(message.chat.id, config.Query.update_state.value, config.StateUser.S_NAME_REQUEST.value)
        elif message.text.lower() == 'помощь':
            bot.send_message(message.chat.id, 'Помощь')
        elif message.text.lower() == 'контакты':
            msg_reply = '\n'.join(config.contacts_arr)
            bot.send_message(message.chat.id, msg_reply)

    @bot.message_handler(func=lambda message: db_worker.get_current_state(
        message.chat.id) == config.StateAdmin.S_START.value)
    def admin_menu(message):
        if message.text.lower() == 'обновить инофрмацию обо мне':
            pass
        elif message.text.lower() == 'добавить контакты':
            pass
        elif message.text.lower() == 'изменить контакты':
            pass
        elif message.text.lower() == 'посмотреть заявки':
            pass

    bot.polling()


if __name__ == '__main__':
    main()