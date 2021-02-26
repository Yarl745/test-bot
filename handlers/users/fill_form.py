import logging

from aiogram.dispatcher import FSMContext
from aiogram.types import Message

import keyboards
from loader import dp
from states import UserForm


@dp.message_handler(state=UserForm.enter_name)
async def read_name(message: Message, state: FSMContext):
    name = message.text
    logging.info(f"User @{message.from_user.username} enters name: {name}")

    if len(name) < 2:
        await message.answer("Очень короткое имя для обезьянего воина 🐒")
        return
    elif len(name) > 20:
        await message.answer("Очень длинное имя для обезьянего воина 🐒")
        return

    await state.update_data(name=name)

    await message.answer("Введи свой возраст:")
    await UserForm.enter_age.set()


@dp.message_handler(state=UserForm.enter_age)
async def read_age(message: Message, state: FSMContext):
    age = message.text
    logging.info(f"User @{message.from_user.username} enters age: {age}")

    if not age.isdecimal():
        await message.answer("Возраст должен вводиться одним целым числом 🐒")
        return

    await state.update_data(age=int(age))

    await message.answer(
        "Какая ты обезьяна?",
        reply_markup=keyboards.default.sex
    )
    await UserForm.enter_sex.set()


@dp.message_handler(state=UserForm.enter_sex)
async def read_sex(message: Message, state: FSMContext):
    sex = message.text
    logging.info(f"User @{message.from_user.username} enters sex: {sex}")

    if sex == "Я мужчина 🙋‍♂️":
        sex = "M"
    elif sex == "Я женщина 🙋‍♀️":
        sex = "W"
    else:
        return

    data = await state.get_data()
    data.update(sex=sex)

    # db.save_user(data)

    await message.answer(
        "Поздравляем! Теперь ты обезьяний воин!",
        reply_markup=keyboards.default.main_menu
    )
    await message.answer_sticker("CAACAgIAAxkBAAMQYDlynYxOoTADvSpTGup5egVVuQ8AAiIDAAJtsEIDvMfD36FwtXgeBA")

    await state.finish()

