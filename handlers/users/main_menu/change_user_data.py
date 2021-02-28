import logging

from aiogram.dispatcher import FSMContext
from aiogram.types import Message

import keyboards
from handlers.users.main_menu.user_config import show_config_menu
from loader import dp, db
from states import UserForm


@dp.message_handler(state=UserForm.change_name, text="Назад ↩️")
@dp.message_handler(state=UserForm.change_age, text="Назад ↩️")
@dp.message_handler(state=UserForm.change_sex, text="Назад ↩️")
async def back_to_config_menu(message: Message):
    await show_config_menu(message)


@dp.message_handler(state=UserForm.change_name)
async def read_name(message: Message):
    name = message.text
    logging.info(f"User @{message.from_user.username} changes name: {name}")

    if len(name) < 2:
        await message.answer("Очень короткое имя для обезьянего воина 🐒")
        return
    elif len(name) > 20:
        await message.answer("Очень длинное имя для обезьянего воина 🐒")
        return

    await db.update_user(user_id=message.from_user.id, name=name)

    await show_config_menu(message)


@dp.message_handler(state=UserForm.change_age)
async def read_age(message: Message):
    age = message.text
    logging.info(f"User @{message.from_user.username} changes age: {age}")

    if not age.isdecimal():
        await message.answer("Возраст должен вводиться одним целым числом 🐒")
        return
    elif len(age) > 3 or int(age) < 0:
        await message.answer("Кажется ты преврал с возрастом... попробуй ввести настоящий возраст 🐒")
        return

    await db.update_user(user_id=message.from_user.id, age=int(age))

    await show_config_menu(message)


@dp.message_handler(state=UserForm.change_sex)
async def read_sex(message: Message):
    sex = message.text
    logging.info(f"User @{message.from_user.username} changes sex: {sex}")

    if sex == "Я мужчина 🙋‍♂️":
        sex = "M"
    elif sex == "Я женщина 🙋‍♀️":
        sex = "W"
    else:
        return

    await db.update_user(user_id=message.from_user.id, sex=sex)

    await show_config_menu(message)