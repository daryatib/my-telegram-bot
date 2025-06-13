import telebot
from telebot import types
import random

API_TOKEN = '8140442640:AAGZMJoUWDUg9y247HUiwW-t9b0TMkgfDdA'
bot = telebot.TeleBot(API_TOKEN)

CAT_MEMES = [
    "https://i.pinimg.com/736x/05/d0/e3/05d0e3691c10c2ee4e1b7c32305cecb3.jpg",
    "https://i.pinimg.com/736x/61/2b/27/612b2742283c0ae75eaecb0c1b9e1b00.jpg",
    'https://i.pinimg.com/736x/40/e5/b8/40e5b8d7e2566a028834b1bffb31fdab.jpg',
    'https://i.pinimg.com/736x/d2/7e/91/d27e91a0eefd866d4f8ab64b4de1e742.jpg',
    'https://i.pinimg.com/736x/f6/6e/b8/f66eb8ad6b45ee22886bb259bfb2c707.jpg',
    'https://i.pinimg.com/736x/2b/8b/54/2b8b5453ac134f51af7bbdc997a8a716.jpg',
    'https://i.pinimg.com/736x/2f/ce/88/2fce884291efcb965c577a5876a60868.jpg',
    'https://i.pinimg.com/736x/c7/80/2a/c7802a548a3c0c0baf633c8dc71b4e04.jpg',
    'https://i.pinimg.com/736x/9e/e7/87/9ee787a94158f8113fbec22a509ed800.jpg',
    'https://i.pinimg.com/736x/4c/78/d1/4c78d11fd2bc4fd065849e1440a0928b.jpg',
    'https://i.pinimg.com/736x/5d/23/b6/5d23b68c3083a0efb921b27c36cfd25c.jpg',
    'https://i.pinimg.com/736x/bb/6c/dc/bb6cdcf84f9875a0b6d0df8e4b237c3d.jpg',

]

DOG_MEMES = [
    'https://i.pinimg.com/736x/e3/e7/af/e3e7af67f943eb4456211515daa749d5.jpg',
    'https://i.pinimg.com/736x/10/d8/78/10d8786127b64099ff8fe278e1d99a5d.jpg',
    'https://i.pinimg.com/736x/21/38/22/21382281b499d9659d0a09f230c265a8.jpg',
    'https://i.pinimg.com/736x/b1/04/15/b10415d97794677b0b5375d3b6ae09de.jpg',
    'https://i.pinimg.com/736x/b3/6e/83/b36e831915287f300c0537394ebd30b3.jpg',
    'https://i.pinimg.com/736x/70/e0/4d/70e04db6870598497d460d0d4ca08c00.jpg',
    'https://i.pinimg.com/736x/d9/d0/34/d9d034d7033b31b4daa6a59db1dab06b.jpg',
    'https://i.pinimg.com/736x/b8/34/4a/b8344ab55912b787c268d21721de474e.jpg',

]

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
        meme_url = random.choice(CAT_MEMES)
        bot.send_photo(message.chat.id, meme_url)
    elif message.text == 'мемы с собаками':
        meme_url = random.choice(DOG_MEMES)
        bot.send_photo(message.chat.id, meme_url)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == 'отстань':
        bot.send_message(message.from_user.id, "сам отстань")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Выбери кнопку")

bot.polling(none_stop=True, interval=0)
