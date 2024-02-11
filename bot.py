import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from config import TOKEN

ALLOWED_UPDATES = ["message", "edited_message"]

bot = Bot(token = TOKEN)

dispatcher = Dispatcher()

# @dispatcher.edited_message()
# async def check_of_changes(message: types.Message):
#     await message.reply(message.from_user.id, "User change the message!")

@dispatcher.message(CommandStart())
async def say_hello(message: types.Message):
    await message.answer("Hello!")

@dispatcher.message()
async def echo(message: types.Message):
    await message.answer(message.text)
    await message.reply(message.text)

async def main():
    await dispatcher.start_polling(bot, allowed_updates=ALLOWED_UPDATES)

asyncio.run(main())