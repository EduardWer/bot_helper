"""Это исполняемый файл где будет прописанна вся суть бота и он сам будет развёртан тут"""
"""Основные функции будут преставленны в файлах конфига или плагинах """
"""В файле recvest.txt будут лежать основные модули для бота """
"""У становить их можно командой pip install -r recvest.txt"""

import os

from aiogram import Bot, types
from aiogram.utils import executor
from aiogram.dispatcher import Dispatcher
import commands_pl
import marku

users_id = your id
password = ''

tokenAPI = 'your token'
bot = Bot(tokenAPI)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start_message(message: types.Message):
    await bot.send_message(message.chat.id, 'Добрый день!,\n'
                                            'Для управления сервером обратитесь к администратору \n'
                                            'выдача права на пользование выдаётся только администрацией!')

    if message.from_user.id != users_id:
        await bot.send_message(message.chat.id, 'Ошибся адресом, дружок')
    else:
        await bot.send_message(message.chat.id, 'Вы прошли авторизацию, ваш id был успешно зарегестрирован.')
        await bot.send_message(message.chat.id, 'Терерь вам доступны все команды сервера.',
                               reply_markup=marku.start_command)


@dp.message_handler()
async def Job(message: types.Message):
    match message.text:
        case "Температура сервера":
            await bot.send_message(message.chat.id, 'Температура ядер')
            await bot.send_message(message.chat.id, commands_pl.temp())
        case "Активные пользователи":
            await  bot.send_message(message.chat.id, f"Вот список активных пользователей  \n {commands_pl.user_add()}")
        case "Процессы сервера":
            await  bot.send_message(message.chat.id, f"Без проблем! \n {commands_pl.process_1()}",
                                    reply_markup=marku.process_markup)
        case "ПЕРЕЗАГРУЗИТЬ":
            await bot.send_message(message.chat.id, 'Сервер перезагружается!', reply_markup=marku.start_command)
            os.system('reload')
        case "Выключить сервер":
            await bot.send_message(message.chat.id, 'Вы уверенны?', reply_markup=marku.shotdown_markup)
        case "ВЫКЛЮЧИТЬ":
            await bot.send_message(message.chat.id, 'Сервер выключается!')
            os.system('shutdown now')
        case "НЕТ ВЫЙТИ":
            await bot.send_message(message.chat.id, 'Хорошо', reply_markup=marku.start_command)


@dp.callback_query_handler(lambda callback_query: callback_query.data and callback_query.data.startswith('btn'))
async def process_adigt(callback_query: types.CallbackQuery):
    code = callback_query.data[-1]
    if code.isdigit():
        code = int(code)
    match code:
        case 1:
         await bot.answer_callback_query(callback_query.id, text='Нажата вторая кнопка')
         await bot.send_message(callback_query.from_user.id, f"{commands_pl.process_1()}",
                               reply_markup=marku.process_markup)
        case 2:
         await bot.send_message(callback_query.from_user.id, f"{commands_pl.process_2()}",
                               reply_markup=marku.process_markup)
        case 3:
         await bot.send_message(callback_query.from_user.id, f"{commands_pl.process_3()}",
                               reply_markup=marku.process_markup)
        case 4:
         await bot.send_message(callback_query.from_user.id, f"{commands_pl.process_4()}",
                               reply_markup=marku.process_markup)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
