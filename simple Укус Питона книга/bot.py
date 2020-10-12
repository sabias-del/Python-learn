from telegram import Bot, Update
from telegram.ext import Updater, MessageHandler, Filters

token = ''  # TOKEN_bot
admin_id = ''  # My ID


def message_handler(bot: Bot, update: Update):
    user = update.effective_user
    if user:
        name = user.fist_name
    else:
        name = 'аноним'
    text = update.effective_message.text
    reply_text = f'Привет,{name}!\n\n{text}'
    bot.send_message(
        chat_id=update.effective_message.chat_id,
        text=reply_text
    )
    return


def main():
    bot = Bot(
        token
    )
    updater = Updater(
        bot, use_context=True
    )
    handler = message_handler(Filters.all, message_handler)
    updater.dispatcher.add_handler(handler)

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
