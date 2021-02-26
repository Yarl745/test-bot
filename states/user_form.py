from aiogram.dispatcher.filters.state import StatesGroup, State


class UserForm(StatesGroup):
    enter_name = State()
    enter_age = State()
    enter_sex = State()
