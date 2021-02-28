import asyncio
import logging

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart, Command
from aiogram.types import ReplyKeyboardRemove

import keyboards
from filters import IsUserExist
from loader import dp
from states import UserForm


@dp.message_handler(Command(["start", "menu"]), IsUserExist(), state="*")
async def bot_start(message: types.Message, state: FSMContext):
    await message.answer(
        "Привет, обезьяний воин! Мы помним тебя.",
        reply_markup=keyboards.default.main_menu
    )
    await message.answer_sticker("CAACAgIAAxkBAANGYDmDFX728Xxi8jfplD7pMOf00ssAAh4DAAJtsEIDqAjz6NCOimgeBA")
    await state.finish()


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    logging.info(f"User @{message.from_user.username} starts bot")

    await message.answer(f"Привет, {message.from_user.full_name}!", reply_markup=ReplyKeyboardRemove())
    await message.answer_sticker("CAACAgIAAxkBAAMGYDloA7-duW0esfV3fMwDGoFgmR8AAv8CAAJtsEIDBKA5qzQCNjceBA")
    await asyncio.sleep(3)

    await message.answer("Пригалашаем тебя в армию обезьян!")
    await message.answer_sticker("CAACAgIAAxkBAAMIYDloFkp_-Oe7Rrcf0pVelf6BfLUAAhUDAAJtsEID164MMR1agW4eBA")
    await asyncio.sleep(3)

    await message.answer("Сначала нам нужно познокомится с тобой.")
    await message.answer("Введи своё имя:")

    await UserForm.enter_name.set()