import telebot
import requests

bot = telebot.TeleBot("8452695730:AAE2d9NkfRk-_45z5S_FDVFNb-rKINYxBG4")

def get_rate():
    try:
        r = requests.get("https://api.tetherland.com/currencies")
        data = r.json()
        usdt = data["data"]["usdt"]["price"]
        return int(usdt)
    except:
        return None

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "👋 سلام! ربات تبدیل دلار و تومان آماده‌ست.\n\nدستورات:\n💵 /t2d مبلغ — تبدیل تومان به دلار\n💰 /d2t مبلغ — تبدیل دلار به تومان\n📈 /rate — نرخ لحظه‌ای")

@bot.message_handler(commands=['rate'])
def rate(message):
    rate = get_rate()
    if rate:
        bot.send_message(message.chat.id, f"📊 نرخ لحظه‌ای دلار:\n💵 1 USD ≈ {rate:,} تومان")
    else:
        bot.send_message(message.chat.id, "❌ خطا در دریافت نرخ!")

@bot.message_handler(commands=['t2d'])
def toman_to_dollar(message):
    try:
        amount = float(message.text.split()[1])
        rate = get_rate()
        usd = amount / rate
        bot.send_message(message.chat.id, f"{amount:,} تومان ≈ {usd:.2f} دلار 💵")
    except:
        bot.send_message(message.chat.id, "❗ مثال:\n/t2d 5000000")

@bot.message_handler(commands=['d2t'])
def dollar_to_toman(message):
    try:
        amount = float(message.text.split()[1])
        rate = get_rate()
        toman = amount * rate
        bot.send_message(message.chat.id, f"{amount} دلار ≈ {toman:,} تومان 💰")
    except:
        bot.send_message(message.chat.id, "❗ مثال:\n/d2t 10")

bot.infinity_polling()
