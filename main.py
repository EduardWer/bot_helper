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

users_id = 'admin id'
password = ''

tokenAPI = 'Your token'
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
            if 'Температура сервера' in message.text:
                await bot.send_message(message.chat.id, 'Температура ядер')
                await bot.send_message(message.chat.id, commands_pl.temp())  # type: ignore

            if 'Процессы сервера' in message.text:
                await bot.send_message(message.chat.id, 'Вот список запущенных процессов')
                await bot.send_message(message.chat.id, commands_pl.process())
            if 'Перезагрузка сервера' in message.text:
                await bot.send_message(message.chat.id, 'Вы точно уверенны?', reply_markup=marku.reload_markup)
            if 'ПЕРЕЗАГРУЗИТЬ' in message.text:
                await bot.send_message(message.chat.id, 'Сервер перезагружается!', reply_markup=marku.start_command)
                os.system('reload')

            if 'Выключить сервер' in message.text:
                await bot.send_message(message.chat.id, 'Вы уверенны?', reply_markup=marku.shotdown_markup)
            if 'ВЫКЛЮЧИТЬ' in message.text:
                await bot.send_message(message.chat.id, 'Сервер выключается!')
                os.system('shutdown now')
            if 'НЕТ ВЫЙТИ' in message.text:
                await bot.send_message(message.chat.id, 'Хорошо', reply_markup=marku.start_command)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
