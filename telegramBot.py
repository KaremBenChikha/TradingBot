import os
from dotenv import load_dotenv
import telebot

load_dotenv()
TELEGRAM_API_KEY = os.getenv('TELEGRAM_API_KEY')
TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')

TelegramBot = telebot.TeleBot(TELEGRAM_API_KEY)

def sendMessage(message):
    TelegramBot.send_message(TELEGRAM_CHAT_ID, message)

def sendArrayMessage(message):
    message = message.to_string()
    TelegramBot.send_message(TELEGRAM_CHAT_ID, message)
