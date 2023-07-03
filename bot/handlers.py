from aiogram import types
# from aiogram.dispatcher import FSMContext

from bot.loader import dp, bot

from users_numbers import Numbers
# from game import RandomGame


numbers_obj = Numbers(0)


@dp.message_handler(commands=['start'], state='*')
async def start_command(message: types.Message):
    if len(message.text.split()) > 1 and message.text.split()[1].isdigit():
        len_users = int(message.text.split()[1])
        global numbers_obj
        numbers_obj = Numbers(len_users)
        await bot.send_message(chat_id=message.chat.id,
                               text=f'Добро пожаловать! Создан список на {len_users} пользователей.\nВведите /number что-бы выдать номера!')
    else:
        await bot.send_message(chat_id=message.chat.id,
                               text=f'Добро пожаловать! Вы не ввели количество игроков!')


@dp.message_handler(commands=['number'], state='*')
async def number_command(message: types.Message):
    global numbers_obj
    if len(numbers_obj.numbers_list) == 1:
        await bot.send_message(chat_id=message.chat.id,
                               text=f'🧮Остался номер: {numbers_obj.numbers_list[0]}')
        numbers_obj.numbers_list.clear()
    elif numbers_obj.numbers_list:
        answer = f'🎰Выдача номера\n📊Диапазон от 🔻1🔻 до 🔺{numbers_obj.len_user}🔺\n🧮Число: {numbers_obj.get_number()}'
        await bot.send_message(chat_id=message.chat.id,
                               text=answer)
    else:
        await bot.send_message(chat_id=message.chat.id,
                               text=f'🗑Список пуст!')


# @dp.message_handler(commands=['game'], state='*')
# async def game_command(message: types.Message):
#     if len(message.text.split()) > 1 and message.text.split()[1].isdigit():
#         last_num = int(message.text.split()[1])
#         await bot.send_message(chat_id=message.chat.id,
#                                text=f'Номер: {RandomGame.random_int(last_num)}')
#     else:
#         await bot.send_message(chat_id=message.chat.id,
#                                text=f'Вы не ввели правую границу!')
