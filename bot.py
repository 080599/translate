import telebot
import botton as bt
bot=telebot.TeleBot(token='7071355758:AAFmykdclGpnx5FoE_h_MpiUn5aq8wwdQ7Q')
@bot.message_handler(commands=['start'])
def start_conversation(message):
    bot.send_message(message.chat.id, "Привет! Я бот-конвертор валют.\nВведите сумму, которую вы хотите конвертировать.", reply_markup=bt.privet_bt())
    bot.register_next_step_handler(message, get_amount)

def get_amount(message):
    try:
        amount = float(message.text)
        bot.send_message(message.chat.id, "Выберите валюту, в которую хотите конвертировать:", reply_markup=bt.konvert_bt())
        bot.register_next_step_handler(message, convert_currency, amount)
    except ValueError:
        bot.send_message(message.chat.id, "Пожалуйста, введите корректное число.")

def convert_currency(message, amount, c=None):
    try:
        currency = message.text
        if currency == "EUR":
            converted_amount = c.convert("UAH", "EUR", amount)
            bot.send_message(message.chat.id, f"{amount} UAH = {converted_amount:.2f} EUR")
        elif currency == "USD":
            converted_amount = c.convert("UAH", "USD", amount)
            bot.send_message(message.chat.id, f"{amount} UAH = {converted_amount:.2f} USD")
        elif currency == "RUB":
            converted_amount = c.convert("UAH", "RUB", amount)
            bot.send_message(message.chat.id, f"{amount} UAH = {converted_amount:.2f} RUB")
        else:
            bot.send_message(message.chat.id, "Неверный выбор валюты.")
    except ValueError:
        bot.send_message(message.chat.id, "Неверный ввод. Попробуйте снова.")


bot.polling()
