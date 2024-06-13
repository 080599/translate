from telebot import types
def privet_bt():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)

    return kb
def konvert_bt():
    kb=types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    markup.add(types.KeyboardButton("EUR"), types.KeyboardButton("USD"), types.KeyboardButton("RUB"))

    return kb
