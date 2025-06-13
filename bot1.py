import telebot
from telebot import types
import random
import requests
from bs4 import BeautifulSoup

API_TOKEN = '8140442640:AAGZMJoUWDUg9y247HUiwW-t9b0TMkgfDdA'
bot = telebot.TeleBot(API_TOKEN)

# ID публичной папки
folder_id_cat = "1TLtX_a6dixMcFtFn308nbjSppwQZOndm"  # Замени на свой
folder_id_dog = "1VCkSQYo98FjCuDW5J-S_soSKFQ4kxtp8"

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("мемы с котами")
    btn2 = types.KeyboardButton("мемы с собаками")
    markup.add(btn1, btn2)
    bot.send_message(
        message.chat.id,
        text="Привет, {0.first_name}! Я бот-мемас".format(message.from_user),
        reply_markup = markup
    )

@bot.message_handler(func=lambda message: message.text in ["мемы с котами", "мемы с собаками"])
def meme(message):
    if message.text == 'мемы с котами':
        url = f"https://drive.google.com/drive/folders/{folder_id_cat}"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        MEMES = [
            f"https://drive.google.com/uc?export=download&id={link.split('/')[5]}"
            for link in str(soup).split('"')
            if '/file/d/' in link
        ]
        meme_url = random.choice(MEMES)
        bot.send_photo(message.chat.id, meme_url)
    elif message.text == 'мемы с собаками':
        url = f"https://drive.google.com/drive/folders/{folder_id_dog}"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        MEMES = [
            f"https://drive.google.com/uc?export=download&id={link.split('/')[5]}"
            for link in str(soup).split('"')
            if '/file/d/' in link
        ]
        meme_url = random.choice(MEMES)
        bot.send_photo(message.chat.id, meme_url)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == 'Привет':
        bot.send_message(message.from_user.id, "Привет! Выбери кнопку")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Выбери кнопку")

bot.polling(none_stop=True, interval=0)
