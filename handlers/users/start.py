import asyncio
import logging

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp
from states import UserForm


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    logging.info(f"User @{message.from_user.username} starts bot")

    await message.answer(f"Привет, {message.from_user.full_name}!")
    await message.answer_sticker("CAACAgIAAxkBAAMGYDloA7-duW0esfV3fMwDGoFgmR8AAv8CAAJtsEIDBKA5qzQCNjceBA")
    await asyncio.sleep(3)

    await message.answer("Пригалашаем тебя в армию обезьян!")
    await message.answer_sticker("CAACAgIAAxkBAAMIYDloFkp_-Oe7Rrcf0pVelf6BfLUAAhUDAAJtsEID164MMR1agW4eBA")
    await asyncio.sleep(3)

    await message.answer("Сначала нам нужно познокомится с тобой.")
    await message.answer("Введи своё имя:")

    await UserForm.enter_name.set()