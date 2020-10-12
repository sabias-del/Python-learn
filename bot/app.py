import config
import logging
import asyncio
from datetime import datetime

from aiogram import Bot, Dispatcher, executor, types
from sqlighter import SQLighter

# Задание уровень логов бота
logging.basicConfig(level=logging.INFO)

# Запуск бота
bot = Bot(token = config.Token)
dp = Dispatcher(bot)
# Соединение с ДБ
db = SQLighter('db.db')
# Команда активации подписки
@dp.message_handler(commands=['subscribe'])
async def subscribe(message: types.Message):
    if(not db.subscriber_exists(message.from_user.id)):
        # если его там нету то создаем запись
        db.add_subscriber(message.from_user.id)
    else:
        # если он уже есть, то просто обновляем ему статус подписки
        db.update_subscribeption(message.from_user.id, True)

    await message.answer("Вы уже подписывались на рассылку!")

# Эхобот
@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
