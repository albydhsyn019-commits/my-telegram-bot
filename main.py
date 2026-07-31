import telebot

# مفتاح البوت الخاص بك
TOKEN = "8631102007:AAGZ3ijUN945H6Xjnc2tLrLBd6CUzg0v-4o"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "أهلاً بك! البوت يعمل بنجاح الآن من السحابة 🚀")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"وصلتني رسالتك: {message.text}")

print("البوت يعمل الآن...")
bot.infinity_polling()
