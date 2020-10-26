import telebot
import config
token = config.Token
# бот модуль телебот + команда что это бот и токен нашего бота
bot = telebot.TeleBot(token)
# вызов класса телебота после отправки команды старат
@bot.message_handler(commands=['start'])
# начать отправлять сообщение после команды старт
def start(message):
    # сент  = бот + отправка собщения любому id text >
    sent = bot.send_message(message.chat.id, 'Как тебя зовут? ')
    # бот регеструет команду и отпрвляет сообщение новому пользователю
    bot.register_next_step_handler(sent, hello)
# создаем функцию самого привествия
def hello(message):
    # бот отправляет сообщение на новый ид
    bot.send_message(message.chat.id, 'Привет, {name}. Рад тебя видеть.'.format(name=message.text))
# запуск бота
bot.polling()
