from aiogram import Dispatcher

from loader import dp
from .is_user_exist import IsUserExist


if __name__ == "filters":
    dp.filters_factory.bind(IsUserExist)
    pass
