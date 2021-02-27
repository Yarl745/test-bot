import logging

from aiogram.dispatcher import FSMContext
from aiogram.types import Message

import keyboards
from filters import IsUserExist
from loader import dp
from states import UserForm


@dp.message_handler(IsUserExist(), text="Настройки ⚙️")
async def show_config_menu(message: Message):
    await message.answer("Подумай, что ты хочешь изменить в своём обезьянем паспорте...",
                         reply_markup=keyboards.default.config_menu)
    await message.answer_sticker("CAACAgIAAxkBAAOPYDmQnSj4wCVjHnlkxNjRBGQoe7QAAgcDAAJtsEIDh9lMXlw897AeBA")

    await UserForm.start_changes.set()


@dp.message_handler(state=UserForm.start_changes, text="Изменить Имя")
async def enter_name(message: Message):
    await message.answer("Введи своё имя:",
                         reply_markup=keyboards.default.back_btn)
    await UserForm.change_name.set()


@dp.message_handler(state=UserForm.start_changes, text="Изменить Возраст")
async def enter_age(message: Message):
    await message.answer("Введи свой возраст:",
                         reply_markup=keyboards.default.back_btn)
    await UserForm.change_age.set()


@dp.message_handler(state=UserForm.start_changes, text="Изменить Пол")
async def enter_sex(message: Message):
    await message.answer("Какая ты обезьяна?",
                         reply_markup=keyboards.default.get_sex(with_back=True))
    await UserForm.change_sex.set()


@dp.message_handler(state=UserForm.start_changes, text="Назад ↩️")
async def back_to_main_menu(message: Message, state: FSMContext):
    logging.info(f"User @{message.from_user.username} backs to main menu")

    await message.answer("Все изменения твоего обезьянего паспорта были сохранены.",
                         reply_markup=keyboards.default.main_menu)
    await message.answer_sticker("CAACAgIAAxkBAAOmYDmeeEHGTFVfDktL8zFjTh-PNMAAAhADAAJtsEIDkuNZ4fNStmkeBA")

    await state.finish()
