import os
import telebot
from flask import Flask, request

# 8631102007:AAGZ3ijUN945H6Xjnc2tLrLBd6CUzg0v-4o
TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"

bot = telebot.TeleBot(TOKEN)
app = Flask(name)

@app.route('/')
def home():
    return "Bot is active and running!"

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "أهلاً بك! البوت يعمل بنجاح الآن على Render 🚀")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"وصلتني رسالتك: {message.text}")

if name == "main":
    import threading
    # تشغيل البوت في مسار جانبي لتجنب إغلاق السيرفر
    threading.Thread(target=bot.infinity_polling, daemon=True).start()
    
    # تشغيل سيرفر Flask على المنفذ المطلوب
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
