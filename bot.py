import telebot

token = '8518911704:AAGYQLajtsRaAF0hCo6GDz91rroY8lualAg'

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Привет, бро! Я твой первый бот. 😎 Напиши что угодно — я повторю.')

@bot.message_handler(func=lambda message: True)
def echo(message):
    bot.reply_to(message, message.text)

print("Бот запущен...")
bot.infinity_polling()