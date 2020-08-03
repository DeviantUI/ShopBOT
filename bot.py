# -*- coding: utf-8 -*-
#import redis
import os
import telebot
#from telebot import types
# import some_api_lib
# import ...

# Example of your code beginning
#           Config vars
token = os.environ['TELEGRAM_TOKEN']
some_api_token = os.environ['SOME_API_TOKEN']

# If you use redis, install this add-on https://elements.heroku.com/addons/heroku-redis
#r = redis.from_url(os.environ.get("REDIS_URL"))

#       Your bot code below
bot = telebot.TeleBot(token)
# some_api = some_api_lib.connect(some_api_token)
#              ...
#Информация
name = 'STICK17 | Shop'
welcome_message = 'STICK 17 выпустили первую линейку футболок с героями фирменных стикерпаков. Коллекция состоит из эмоций, которые ежедневно испытывает каждый из нас. Высокое качество. Ограниченный тираж. Бесплатная доставка на территории РФ.'
information = 'г. Барнаул\nпр-т Социалистический, 34\nофис 302\nstick17@lenta.ru\n+79833589069\nwww.stick17.ru'
contact= '@stick17_shop_bot'
#Дальше в код лезть не советую
#             ...
img = 'img/logo.jpg'

keyboard = telebot.types.ReplyKeyboardMarkup(True)
keyboard.row('Витрина', 'Услуги')

keyboard2 = telebot.types.ReplyKeyboardMarkup(True)
keyboard2.row('Футболки')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    ###log
    #l = open('log.txt', 'a', encoding="utf-8")
    #l.write('id : ' + str(message.from_user.id) + '\nusername : ' + str(message.from_user.username) + '\nlanguage_code : ' + str(message.from_user.language_code) + '\ntext : ' + str(message.text) + '\n\n')
    #l.close()
    ###
    if message.text == "/start":
        bot.send_photo(message.chat.id, open(img, 'rb'), welcome_message, reply_markup=keyboard)
    elif message.text == "Витрина":
        bot.send_photo(message.from_user.id, open(img, 'rb'), name + '\n' + information)
    elif message.text == "Услуги":
        mas = []
        f = open('BD.txt', "r", encoding="utf-8")
        n  = int(f.readline())
        f.readline()
        for i in range(n):
            mas.append([])
            for j in range(5):
                mas[i].append(f.readline())
            f.readline()
        for i in range(n):
            bot.send_photo(message.from_user.id, mas[i][4], mas[i][0]+mas[i][1]+mas[i][2]+mas[i][3] + 'Контакты: ' + contact)
        f.close()
    elif message.text == "Услуги1":
        bot.send_message(message.from_user.id, 'Здесь будет список услуг')
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /start.")

@bot.message_handler(content_types=['sticker'])
def sticker_id(message):
    print(message)

bot.polling(none_stop=True, interval=0)
