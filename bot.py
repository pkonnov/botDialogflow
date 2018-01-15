from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import apiai, json


# token from bots telegram
updater = Updater(token='API from telegram bots')
dispatcher = updater.dispatcher

def startCommand(bot, update):
	bot.send_message(chat_id=update.message.chat_id, text='Привет, давай общаться?')

def textMessage(bot, update):
	request = apiai.ApiAI('Client access token from Dailogflow').text_request()
	request.lang = 'ru'
	request.session_id = 'NameBot'
	request.query = update.message.text
	responseJson = json.loads(request.getresponse().read().decode('utf-8'))
	response = responseJson['result']['fulfillment']['speech']
	if response:
		bot.send_message(chat_id=update.message.chat_id, text=response)
	else:
		bot.send_message(chat_id=update.message.chat_id, text='Я вас не совсем понял')


start_command_handler = CommandHandler('start,', startCommand)
text_message_handler = MessageHandler(Filters.text, textMessage)

dispatcher.add_handler(start_command_handler)
dispatcher.add_handler(text_message_handler)

updater.start_polling(clean=True)
