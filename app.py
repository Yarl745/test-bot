from aiogram import executor

from loader import dp, db, scheduler
import middlewares, filters, handlers
from utils.notify_admins import on_startup_notify
from utils.schedule_jobs import schedule_jobs
from utils.set_commands import register_commands


async def on_startup(dispatcher):
    await on_startup_notify(dispatcher)

    await register_commands()
    schedule_jobs()

    await db.create_table_users()
    await db.create_table_hour_clicks()
    await db.set_timezone()


if __name__ == '__main__':
    scheduler.start()
    executor.start_polling(dp, on_startup=on_startup)