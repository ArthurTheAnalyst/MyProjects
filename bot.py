import telebot
from telebot import types

with open('bottoken.txt') as f:
    lines = f.readlines()

token = ''

for line in lines:
    token += line

bot = telebot.TeleBot(token)

@bot.message_handler(commands=["start"])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("🇷🇺 Русский")
    btn2 = types.KeyboardButton('🇬🇧 English')
    markup.add(btn1, btn2)
    bot.send_message(message.from_user.id, "🇷🇺 Выберите язык / 🇬🇧 Choose your language", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    if message.text == "🇷🇺 Русский":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
        btn1 = types.KeyboardButton("👁‍🗨 Расскажи мне об Артуре")
        btn2 = types.KeyboardButton("💬 Как связаться с Артуром?")
        btn3 = types.KeyboardButton("🔙 Главное меню / Main menu")
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id, "Салют! \nЯ личный бот Артура \nРасскажу Вам о нём и помогу с ним связаться.", reply_markup=markup)
        bot.send_message(message.from_user.id, "Сделайте свой выбор:")

    elif message.text == "👁‍🗨 Расскажи мне об Артуре":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        bot.send_message(message.from_user.id, "Вот что у меня есть про Артура: \n🔘 Прежде всего, я - его первый проект \n🔘 Артур является студентом 4 курса направления Экономика \n🔘 22 года \n🔘 г. Москва", parse_mode='Markdown')

    elif message.text == "💬 Как связаться с Артуром?":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Главное меню / Main menu')
        markup.add(btn1)
        bot.send_message(message.from_user.id, " [Vk](https://vk.com/id347590404) \n[Telegram](https://t.me/ArthurTheDstr) \n[Mail](https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox?compose=GTvVlcRwPkVKfgtTvCvCBJQwPrndlPtDXHtjmjCxfzZLSdTGxvVhQKFsghkJvVRlkhxdSVfmJTlbc)", parse_mode='Markdown')

    elif message.text == "🔙 Главное меню / Main menu":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🇷🇺 Русский")
        btn2 = types.KeyboardButton("🇬🇧 English")
        markup.add(btn1,btn2)
        bot.send_message(message.from_user.id, "🇷🇺 Выберите язык / 🇬🇧 Choose your language", reply_markup=markup)

    if message.text == "🇬🇧 English":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
        btn1 = types.KeyboardButton("👁‍🗨 Tell me about Arthur")
        btn2 = types.KeyboardButton("💬 How can I contact Arthur?")
        btn3 = types.KeyboardButton("🔙 Main menu / Главное меню")
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id, "Nice to see you, Comrad! \nI am Arthur's personal bot. \nI will tell you about him and help you contact him.", reply_markup=markup)
        bot.send_message(message.from_user.id, "Choose an option:")


    elif message.text == "👁‍🗨 Tell me about Arthur":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Main menu / Главное меню')
        markup.add(btn1)
        bot.send_message(message.from_user.id, "Here's what I have about Arthur: \n🔘 First of all, I'm his first project \n🔘 Arthur is a fourth-year student of Economics \n🔘 22 years old \n🔘 Moscow.", parse_mode='Markdown')

    elif message.text == "💬 How can I contact Arthur?":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🔙 Main menu / Главное меню")
        markup.add(btn1)
        bot.send_message(message.from_user.id, " [Vk](https://vk.com/id347590404) \n[Telegram](https://t.me/ArthurTheDstr) \n[Mail](https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox?compose=GTvVlcRwPkVKfgtTvCvCBJQwPrndlPtDXHtjmjCxfzZLSdTGxvVhQKFsghkJvVRlkhxdSVfmJTlbc)", parse_mode='Markdown')

    elif message.text == "🔙 Main menu / Главное меню":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🇷🇺 Русский")
        btn2 = types.KeyboardButton("🇬🇧 English")
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, "🇷🇺 Выберите язык / 🇬🇧 Choose your language", reply_markup=markup)


dddd
bot.polling(none_stop=True, interval=0)