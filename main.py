import telebot
import config
import keybord

bot = telebot.TeleBot(config.TOKEN)


def main():
    @bot.message_handler(commands=['start'])
    def start_msg(message):
        bot.send_message(message.chat.id, 'Приветствую Вас', reply_markup=keybord.key_board_start)

    @bot.message_handler(content_types=['text'])
    def send_msg(message):
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