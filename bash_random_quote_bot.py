# BashRandomQuoteBot бот для Телеграм, который выдает случайную цитату с bash.im
import requests
from bs4 import BeautifulSoup
import telebot #подключаем библиотеку для работы с ботом

bot = telebot.TeleBot('1023021830:AAF4KuD-FIjgAvLLomcvb5HOxtZWVrVZ0JQ')
 
from telebot import types

@bot.message_handler(content_types=['text'])

def get_text_messages(message):
    keyboard = types.InlineKeyboardMarkup()
    key_quote = types.InlineKeyboardButton(text='Цитата', callback_data='quote')
    keyboard.add(key_qoute)
    bot.send_message(reply_markup=keyboard)
    
@bot.callback_query_handler(func=lambda call: True)

def callback_worker(call):

    url = 'https://bash.im/random'    
    text = get_text(url)
    if call.data == 'quote': 
        bot.send_message(call.message.chat.id, text)
        
def get_text(url):
    rs = requests.get(url)
    root = BeautifulSoup(rs.content, 'html.parser')
    article = root.select_one('article')

    return article.text


bot.polling(none_stop=True, interval=0)

    