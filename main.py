from dotenv import load_dotenv
import telegram.ext
import requests
import telebot
import json
import os

#from telegram.bot import Bot

load_dotenv()
# TOKEN = os.environ['TOKEN'] # for running it in replit -- create secret credentials for TOKEN
TOKEN= os.getenv("TOKEN")
bot = telebot.TeleBot(TOKEN)
updater = telegram.ext.Updater(
  TOKEN, use_context=True)  #Replace TOKEN with your token string
dispatcher = updater.dispatcher


#hello world response
def hello(update, context):
  update.message.reply_text(chat_id=update.effective_chat.id,
                            text='Hello, This is a telegram bot')


#rest api hit and get data
def summary(update, context):
  response = requests.get('https://api.covid19api.com/summary')
  if (response.status_code == 200):  #Everything went okay, we have the data
    data = response.json()
    print(data['Global'])
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=data['Global'])
  else:  #something went wrong
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Error, something went wrong.")


corona_summary_handler = telegram.ext.CommandHandler('summary', summary)
dispatcher.add_handler(corona_summary_handler)

#If hello comes to bot it will redirect to hello method

hello_handler = telegram.ext.CommandHandler('hello', hello)
dispatcher.add_handler(hello_handler)


def electronic(update, context):
  response = requests.get('https://dummyjson.com/products/search?q=Laptop')
  if (response.status_code == 200):  #Everything went okay, we have the data
    data = response.json()
    print(data['products'])
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=data['products'])
  else:  #something went wrong
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Error, something went wrong.")


electronic_summary_handler = telegram.ext.CommandHandler(
  'electronic', electronic)
dispatcher.add_handler(electronic_summary_handler)


# For Commands
def fnc1(update, context):
  bot.send_message(
    chat_id=update.effective_chat.id,
    text="Welcome to the www.praveensingampalli.com ",
  )


start_value2 = telegram.ext.CommandHandler('start', fnc1)
dispatcher.add_handler(start_value2)


#adding more Command
def fnc2(update, context):
  bot.send_message(
    chat_id=update.effective_chat.id,
    text="tutorial link: wwww.youtube.com/praveensingampalli ",
  )


start_value = telegram.ext.CommandHandler('youtube', fnc2)
dispatcher.add_handler(start_value)

updater.start_polling()
updater.idle()