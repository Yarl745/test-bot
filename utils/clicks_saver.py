import logging
from datetime import datetime

from loader import activity_saver, db


async def save_hour_clicks():
    hour_clicks = activity_saver.get_count_hour_clicks()
    activity_saver.clear_hour_clicks_counter()

    time = datetime.now().strftime("%H:%M:%S")
    logging.info(f"Save hours_clicks {time} -- users made {hour_clicks} clicks")

    await db.set_hour_clicks(hour_clicks)
