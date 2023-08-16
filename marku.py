from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

temp_button = KeyboardButton('Температура сервера')
process = KeyboardButton('Процессы сервера')
reload = KeyboardButton('Перезагрузка сервера')
shotdown = KeyboardButton('Выключить сервер')
start_command = ReplyKeyboardMarkup(resize_keyboard=True).add(temp_button, process, reload, shotdown)

shotdown_True = KeyboardButton('ВЫКЛЮЧИТЬ')
exits = ('НЕТ ВЫЙТИ')
shotdown_markup = ReplyKeyboardMarkup(resize_keyboard=True).add(shotdown_True, exits)

reload_button = KeyboardButton('ПЕРЕЗАГРУЗИТЬ')
reload_markup = ReplyKeyboardMarkup(resize_keyboard=True).add(reload_button, exits)
