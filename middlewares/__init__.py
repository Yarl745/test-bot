from aiogram import Dispatcher

from loader import dp
from .throttling import ThrottlingMiddleware
from .clicker import ClickerMiddleware


if __name__ == "middlewares":
    dp.middleware.setup(ThrottlingMiddleware())
    dp.middleware.setup(ClickerMiddleware())