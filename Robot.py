import telebot
import random

bot = telebot.TeleBot("8462658571:AAGNPAy8MY8Khgr3FkcAyFkgGnLzlL6Pfxc")
motivational_quotes = [
    "دنبال یه دلیل برای پرواز بگرد حتی وقتی هزار دلیل برای سقوط داری...",
    "گاهی باید بدترین دردها رو بکشی تا بهترین تغییرها رو تجربه کنی...",
    "زندگی آسون‌تر نمیشه، تو قوی‌تر شو.",
    "هر غروبی طلوعی دارد.",
    "برای چیزهایی که می‌خوای تلاش کن، نه آرزو!",
    "اولش سخته، ولی تهش قشنگه."
]
@bot.message_handler(func=lambda m: m.text == "سلام")
def hi(msg):
    bot.send_message(msg.chat.id, "خوش اومدی خوشتیپ یک جمله انگیزشی میخوای؟ پس کامند جمله انگیزشی رو بزن.")

@bot.message_handler(commands=('command0'))
def start(msg):
    bot.send_message(msg.chat.id, random.choice(motivational_quotes))


bot.infinity_polling()
