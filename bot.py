import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from config import TOKEN

bot = Bot(token = TOKEN)

dispatcher = Dispatcher()

@dispatcher.message(CommandStart())
async def say_hello(message: types.Message):
    await message.answer("Hello!")

@dispatcher.message()
async def echo(message: types.Message):
    await message.answer(message.text)
    await message.reply(message.text)

async def main():
    await dispatcher.start_polling(bot)

asyncio.run(main())