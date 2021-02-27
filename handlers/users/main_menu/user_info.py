import logging

from aiogram.types import Message

from filters import IsUserExist
from loader import dp, db


@dp.message_handler(IsUserExist(), text="Обезьяний паспорт 🐒")
async def get_user_info(message: Message):
    logging.info(f"User @{message.from_user.username} requests user info")

    data = await db.get_user_data_by_id(message.from_user.id)
    name = data['name']
    age = data['age']
    sex = "Самец" if data['sex'] == "M" else "Самка"

    await message.answer(
        f"🐒Обезьяний паспорт🐒\n"
        f"Имя: {name}\n"
        f"Возраст: {age} лет\n"
        f"Пол: {sex}"
    )

