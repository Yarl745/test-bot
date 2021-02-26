from aiogram import executor

from loader import dp, db
import middlewares, filters, handlers
from utils.notify_admins import on_startup_notify


async def on_startup(dispatcher):
    await on_startup_notify(dispatcher)

    await db.create_table_users()


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
