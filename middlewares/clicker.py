import logging

from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.types import Message, ReplyKeyboardMarkup

from loader import activity_saver


class ClickerMiddleware(BaseMiddleware):
    async def on_process_message(self, message: Message, data: dict):
        activity_saver.save_click(message.from_user.id)