from aiogram.dispatcher.filters.state import StatesGroup, State


class UserForm(StatesGroup):
    enter_name = State()
    enter_age = State()
    enter_sex = State()

    start_changes = State()
    change_name = State()
    change_age = State()
    change_sex = State()
