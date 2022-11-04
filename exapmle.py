from telegram.ext import Updater,  MessageHandler, Filters
import json
def echo (update,context):
    chat_id = update.message.chat.id
    text = update.message.text
    bot = context.bot
    f = open('data.json').read()
    data = json.loads(f)
    
    like = data.get('LIKE')
    dislike = data.get('DISLIKE')
    if text == '👍':
        like+=1
    if text == '👎':
        dislike+=1
    
    data['LIKE'] = like
    data['DISLIKE'] = dislike
    data = json.dumps(data)
    f = open('data.json','w')
    f.write(data)
    f.close()

    bot.sendMessage(chat_id,f"👍:{like}\n\n👎:{dislike}")

updater = Updater('5643654386:AAGaxNP-8Kkwzi8Ko047p0BZBd3t6a0eIu4')

updater.dispatcher.add_handler(MessageHandler(Filters.text,echo))

updater.start_polling()
updater.idle()