import requests
from bs4 import BeautifulSoup
import telebot
print('Все библиотеки загружены')

bot = telebot.TeleBot('The bot token should be here')
 
from telebot import types

@bot.message_handler(content_types=['text'])

def get_text_messages(message):
        bot.send_message(message.from_user.id, "А вот и я, а вот и кнопочка моя: ")
        keyboard = types.InlineKeyboardMarkup()
        key_quote = types.InlineKeyboardButton(text='Цитата', callback_data='quote')
        keyboard.add(key_quote)
        bot.send_message(message.from_user.id, text='Нажми на кнопку', reply_markup=keyboard)
    
@bot.callback_query_handler(func=lambda call: True)

def callback_worker(call):
  
    if call.data == 'quote': 
        url = 'https://bash.im/random'    
        #text = get_text(url)
        rs = requests.get(url)
        root = BeautifulSoup(rs.content, 'html.parser')
        article = root.select_one('article')
        bot.send_message(call.message.chat.id, article.text)
        
bot.polling(none_stop=True, interval=0)
