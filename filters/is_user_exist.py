from aiogram.dispatcher.filters import BoundFilter
from aiogram.types import Message

from loader import db


class IsUserExist(BoundFilter):
    async def check(self, msg: Message, *args) -> bool:
        return await db.is_user_exist(msg.from_user.id)