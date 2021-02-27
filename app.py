from aiogram import executor

from loader import dp, db
import middlewares, filters, handlers
from utils.notify_admins import on_startup_notify
from utils.set_commands import register_commands


async def on_startup(dispatcher):
    await on_startup_notify(dispatcher)

    await register_commands()

    await db.create_table_users()


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
