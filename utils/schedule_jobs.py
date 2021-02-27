import logging
from datetime import datetime, timedelta

from loader import scheduler
from utils.clicks_saver import save_hour_clicks


def schedule_jobs():
    logging.info("All jobs scheduled")

    # Make even start datetime (for example 04:21 --> 04:00)
    now = datetime.now()
    start_date = now - timedelta(minutes=now.minute)

    scheduler.add_job(save_hour_clicks, "interval", hours=1, start_date=start_date)