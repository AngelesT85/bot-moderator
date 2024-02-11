import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from time import time
time_start = time()

bot = Bot(token = "6983802838:AAHF9Lm4bWZIXJr77u4RpafcUCjUIkKEeOY")

dispatcher = Dispatcher()

@dispatcher.message(CommandStart())
async def rise_my_eyelids(message: types.Message):
    now_time = time()
    if (now_time - time_start) % 604800 == 0:
        await bot.send_message(message.from_user.id, "rise_my_eyelids!".upper())

async def main():
    await dispatcher.start_polling(bot)

asyncio.run(main())