import telebot
from bot_logic import gen_pass
import random
    
bot = telebot.TeleBot("7923037076:AAEm98IRSvCydzSUaLJlry9xV3J7ngeo0As")

eco_data = {
    "батарейка": {
        "куда": "Сдать в пункт приёма опасных отходов или в специальные контейнеры в магазинах.",
        "разлагается": "От 100 до 110 лет.",
        "переработка": "Около 1 года."
    },
    "пластиковая бутылка": {
        "куда": "В контейнер для пластика.",
        "разлагается": "Около 450 лет.",
        "переработка": "Несколько недель."
    },
    "банановая кожура": {
        "куда": "В контейнер для органических отходов или компост.",
        "разлагается": "2-4 недели.",
        "переработка": "Разлагается естественным образом."
    },
    "старый телефон": {
        "куда": "Сдать в пункт приёма техники или магазины с программой утилизации.",
        "разлагается": "До 1000 лет (если просто выбросить).",
        "переработка": "Металлы и пластик перерабатываются за 1-3 месяца."
    },
    "джинсы": {
        "куда": "Сдать в пункт приёма одежды или отдать на переработку текстиля.",
        "разлагается": "1-3 года (хлопок), синтетика — дольше.",
        "переработка": "До 2 месяцев."
    }
}

@bot.message_handler(commands=['start', 'welcome'])
def send_welcome(message):
            bot.reply_to(message, "Привет! Я твой Telegram бот. Напиши /info чтобы узнать что я умею!")

@bot.message_handler(commands=['info'])
def send_info(message):
        info_text = ("Вот что я умею: \n" 
                     "/start and /welcome"
                     "/hello"
                     "/great"
                     "/bye"
                     "/password"
                     "/quiz"
                     "/weather"
                     ) 
        bot.reply_to(message, info_text)
        
@bot.message_handler(commands=['weather'])
def send_weather(message):
    msg = bot.reply_to(message, "Введи название города, и я скажу тебе погоду (фейковую):")
    bot.register_next_step_handler(msg, fake_weather)

def fake_weather(message):
    city = message.text.strip()
    temperatures = ['+20°C ', '+15°C ', '+10°C ', '+25°C ', '+18°C ', '+5°C ']
    forecast = random.choice(temperatures)
    bot.reply_to(message, f"Погода в городе {city} сегодня: {forecast} (прогноз фейковый)")

@bot.message_handler(commands=['quiz'])
def send_quiz(message):
    question = "Какой язык чаще всего используется для Telegram-ботов?"
    options = [
        "1. Python",
        "2. Java",
        "3. C++",
        "4. HTML"
    ]
    quiz_text = question + "\n" + "\n".join(options) + "\n\nНапиши номер правильного ответа:"
    msg = bot.send_message(message.chat.id, quiz_text)
    bot.register_next_step_handler(msg, check_quiz_answer)

def check_quiz_answer(message):
    if message.text.strip() == "1":
        bot.send_message(message.chat.id, "Правильно! Это Python.")
    else:
        bot.send_message(message.chat.id, "Неправильно. Правильный ответ: 1. Python")
        
@bot.message_handler(commands=['hello'])
def send_hello(message):
            bot.reply_to(message, "Привет! Как дела?")

@bot.message_handler(commands=['great'])
def send_great(message):
            bot.reply_to(message, "Рад слышать! у меня тоже все супер.")

        
@bot.message_handler(commands=['bye'])
def send_bye(message):
            bot.reply_to(message, "Пока! Удачи!")

@bot.message_handler(commands=['password'])
def send_password(message):
            password = gen_pass(10)
            bot.reply_to(message, "Вот твой пароль:" + password)

@bot.message_handler(commands=['greenworld'])
def send_greenworld(message):
       with open("images/world.webp", 'rb') as f:
              bot.send_photo(message.chat.id, f)

@bot.message_handler(commands=['ecology'])
def send_password(message):
            bot.reply_to(message, "Нужно беречь природу!")

@bot.message_handler(commands=['eco'])
def eco_start(message):
    message = bot.reply_to(message, "Напиши название предмета, и я расскажу, куда его выбросить и сколько он разлагается.")
    bot.register_next_step_handler(message, eco_info)

def eco_info(message):
    item = message.text.strip().lower()
    if item in eco_data:
        info = eco_data[item]
        reply_text = "Информация по предмету: " + item.capitalize() + "\n"
        reply_text += "Куда выбросить: " + info['куда'] + "\n"
        reply_text += "Разлагается: " + info['разлагается'] + "\n"
        reply_text += "Переработка: " + info['переработка']
        bot.reply_to(message, reply_text)
    else:
        bot.reply_to(message, "Извини, у меня нет данных по этому предмету. Попробуй другой.")
        
        
@bot.message_handler(func=lambda message: True)
def echo_all(message):
            bot.reply_to(message, message.text)
        
bot.polling()