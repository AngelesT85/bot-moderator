import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart


bot = Bot(token = "6983802838:AAHF9Lm4bWZIXJr77u4RpafcUCjUIkKEeOY")

dispatcher = Dispatcher()


@dispatcher.message(CommandStart())
async def start_command(message: types.Message):
    await message.answer("It was start")


@dispatcher.message()
async def echo_message(message: types.Message, bot: Bot):
    await bot.send_message(message.from_user.id, "Я жив!")
    await message.answer(message.text)
 
 


async def main():
    await dispatcher.start_polling(bot)



asyncio.run(main())