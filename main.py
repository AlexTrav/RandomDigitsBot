from aiogram import executor
from bot.loader import dp
from bot import handlers


if __name__ == '__main__':
    executor.start_polling(dispatcher=dp, skip_updates=True)
