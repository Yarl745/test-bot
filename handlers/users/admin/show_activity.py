import logging
from datetime import timedelta, datetime

from aiogram.dispatcher.filters import Command
from aiogram.types import Message

from data.config import ADMINS
from loader import dp, db, activity_saver


@dp.message_handler(Command("show_activity"), chat_id=ADMINS, state="*")
async def show_activity(message: Message):
    logging.info("Show users activity for admin")

    day_hour_clicks = await db.get_24_hour_clicks()

    # Example one output string --> 11:00-12:00  —>  324
    info_activity = f"\n".join(
        [
            f"{(hour_clicks['saving_date']-timedelta(hours=1)).strftime('%H:%M')}-"
            f"{hour_clicks['saving_date'].strftime('%H:%M')}  —>"
            f"  {hour_clicks['clicks']}"
            for hour_clicks in day_hour_clicks
        ]
    )

    now = datetime.now()
    сurrent_activity = f"Новое {(now-timedelta(minutes=now.minute)).strftime('%H:%M')}-" \
                       f"{now.strftime('%H:%M')}  —>  {activity_saver.get_count_hour_clicks()}"

    await message.answer(
        f"Информация по активным пользователям за 24 часа:\n\n"
        f"{info_activity}\n\n"
        f"{сurrent_activity}"
    )