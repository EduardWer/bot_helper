from aiogram.types import KeyboardButton, ReplyKeyboardMarkup , InlineKeyboardButton,InlineKeyboardMarkup

temp_button = KeyboardButton('Температура сервера')
process = KeyboardButton('Процессы сервера')
user_list = KeyboardButton("Активные пользователи")
reload = KeyboardButton('Перезагрузка сервера')
shotdown = KeyboardButton('Выключить сервер')
start_command = ReplyKeyboardMarkup(resize_keyboard=True).add(temp_button, process,user_list, reload, shotdown)

shotdown_True = KeyboardButton('ВЫКЛЮЧИТЬ')
exits = ('НЕТ ВЫЙТИ')
shotdown_markup = ReplyKeyboardMarkup(resize_keyboard=True).add(shotdown_True, exits)

reload_button = KeyboardButton('ПЕРЕЗАГРУЗИТЬ')
reload_markup = ReplyKeyboardMarkup(resize_keyboard=True).add(reload_button, exits)



first_list = InlineKeyboardButton("▶",callback_data="btn1")
second_list = InlineKeyboardButton("⏩",callback_data="btn2")
third_list = InlineKeyboardButton("⏭",callback_data="btn3")
fourths_list = InlineKeyboardButton("⏩⏭",callback_data="btn3")
process_markup= InlineKeyboardMarkup().add(first_list,second_list,third_list,fourths_list)
