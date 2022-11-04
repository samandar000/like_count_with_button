from telegram.ext import (
    Updater,
    CommandHandler, 
    MessageHandler, 
    Filters,
    InlineQueryHandler,
    CallbackQueryHandler
)
from pprint import pprint
import json
from telegram import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
def start(update, context):
    chat_id = update.message.chat.id
    bot = context.bot

    bot.sendMessage(chat_id, 'Welcome!')

def echo(update, context):
    chat_id = update.message.chat.id
    text = update.message.text
    bot = context.bot
    button1 = KeyboardButton(text='Cat')
    button2 = KeyboardButton(text='Dog')
    button3 = KeyboardButton(text='Inline')

    reply_markup =ReplyKeyboardMarkup(
        [
            [button1, button2],
            [button3]
        ],
        resize_keyboard=True)

    bot.sendMessage(chat_id, text, reply_markup=reply_markup)

def inlinekeyboard(update, context):
    chat_id = update.message.chat.id
    text = update.message.text
    bot = context.bot
    like = InlineKeyboardButton(
        text='👍', 
        callback_data='like'
        )
    dislike = InlineKeyboardButton(
        text='👎', 
        callback_data='dislike')
    keyboard = InlineKeyboardMarkup([[like, dislike]])
    photo='https://www.simplilearn.com/ice9/free_resources_article_thumb/Types_of_Artificial_Intelligence.jpg'
    
    bot.sendPhoto(chat_id, photo=photo, reply_markup = keyboard)

def callback_inline(update, context):
    query = update.callback_query
    callback_data = query.message.reply_markup.inline_keyboard[0]
    print(callback_data[0],callback_data[1])
    query.answer(text='Done! ✅')
updater = Updater("5643654386:AAGaxNP-8Kkwzi8Ko047p0BZBd3t6a0eIu4")

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(MessageHandler(Filters.text('Inline'), inlinekeyboard))
updater.dispatcher.add_handler(MessageHandler(Filters.text, echo))
updater.dispatcher.add_handler(CallbackQueryHandler(callback_inline,pattern='like'))
updater.start_polling()
updater.idle()