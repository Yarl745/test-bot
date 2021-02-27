import logging
from datetime import timedelta

from aiogram.dispatcher.filters import Command
from aiogram.types import Message

from data.config import ADMINS
from loader import dp, db


@dp.message_handler(Command("show_activity"), chat_id=ADMINS, state="*")
async def show_activity(message: Message):
    logging.info("Show users activity for admin")

    day_hour_clicks = await db.get_24_hour_clicks()

    # Example one output string --> 11:00-12:00  —>  324
    info = f"\n".join(
        [
            f"{(hour_clicks['saving_date']-timedelta(hours=1)).strftime('%H:%M')}-"
            f"{hour_clicks['saving_date'].strftime('%H:%M')}  —>"
            f"  {hour_clicks['clicks']}"
            for hour_clicks in day_hour_clicks
        ]
    )

    await message.answer(
        f"Информация по активным пользователям за 24 часа:\n\n"
        f"{info}"
    )