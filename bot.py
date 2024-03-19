from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext


TOKEN = '6687558196:AAGJP4pEgYSKQroaxPh44Jd0M_3frOz4vfk'
bot = Bot(TOKEN)
dp = Dispatcher()


@dp.message(Command(commands=["start"]))
async def command_handler(message: types.Message, state: FSMContext) -> None:
    await message.answer("Hello, new user!")


@dp.message()
async def echo_handler(message: types.Message, state: FSMContext) -> None:
    await message.answer(message.text)


if __name__ == '__main__':
    dp.run_polling(bot)
