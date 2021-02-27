import asyncio
import logging

import asyncpg
from asyncpg import Pool

from data import config


class Database:
    def __init__(self, pool: Pool) -> None:
        self.pool: Pool = pool


    @classmethod
    async def create(cls):
        logging.info("Connect to Postgresql Database")

        pool = await asyncpg.create_pool(
            user=config.PG_USER,
            password=config.PG_PASSWORD,
            database=config.PG_DB,
            host=config.IP
        )
        return cls(pool)


    async def set_timezone(self):
        logging.info("Set my Time Zone")

        sql = """
            ALTER DATABASE test_db SET timezone TO 'EET';    
        """
        await self.pool.execute(sql)


    async def create_table_users(self):
        logging.info("Creat Users Table (if not exist)")

        sql = """
            CREATE TABLE IF NOT EXISTS Users(
                id INTEGER PRIMARY KEY,
                username VARCHAR(64) NOT NULL,
                name VARCHAR(20) NOT NULL,
                age INTEGER NOT NULL,
                sex VARCHAR(1) NOT NULL
            );
        """
        await self.pool.execute(sql)


    async def create_table_hour_clicks(self):
        logging.info(f"Create HourClicks table (if not exist)")

        sql = """
            CREATE TABLE IF NOT EXISTS HourClicks(
               saving_date TIMESTAMP PRIMARY KEY DEFAULT CURRENT_TIMESTAMP,
               clicks SMALLINT 
            );
        """
        await self.pool.execute(sql)


    async def get_24_hour_clicks(self) -> list:
        logging.info(f"Get last 24 hours clicks statistic")

        sql = """
            SELECT * FROM HourClicks
                WHERE saving_date > NOW() - INTERVAL '24 hours';
        """
        return await self.pool.fetch(sql)


    async def set_hour_clicks(self, clicks: int):
        logging.info(f"Set hour clicks: {clicks}")

        sql = """
            INSERT INTO HourClicks(clicks) VALUES ($1);
        """
        await self.pool.execute(sql, clicks)


    async def add_user(self, **kwargs):
        logging.info(f"Add new user: {kwargs}")

        columns = ", ".join(kwargs.keys())
        nums = ", ".join([
            f"${num}" for num in range(1, len(kwargs) + 1)
        ])
        sql = """
            INSERT INTO Users({columns}) VALUES ({nums})
            ON CONFLICT DO NOTHING;
        """.format(columns=columns, nums=nums)
        await self.pool.execute(sql, *kwargs.values())


    async def update_user(self, user_id, **kwargs):
        logging.info(f"Update user--{user_id}'s values: {kwargs}")

        updated_fields = ", ".join([
            f"{item}=${num}" for num, item in enumerate(kwargs, start=1)
        ])
        sql = """
            UPDATE Users 
            SET {updated_fields}
            WHERE id={user_id}; 
        """.format(updated_fields=updated_fields, user_id=user_id)
        await self.pool.execute(sql, *kwargs.values())


    async def get_user_data_by_id(self, user_id):
        logging.info(f"Get user--{user_id}")

        sql = """
            SELECT * FROM Users
                WHERE id = $1;
        """
        return await self.pool.fetchrow(sql, user_id)


    async def get_all_users(self):
        logging.info(f"Get all users from Users db")

        sql = """
            SELECT * FROM Users;
        """
        return await self.pool.fetch(sql)


    async def delete_all_users(self):
        logging.info(f"Delete all users from Users db")

        sql = """
            DELETE FROM Users WHERE True;
        """
        await self.pool.execute(sql)


    async def is_user_exist(self, user_id):
        return True if await self.get_user_data_by_id(user_id) else False


# async def test_hour_clicks_table():
#     db = await Database.create()
#
#     await db.create_table_hour_clicks()
#
#     # for i in range(3):
#     #     await db.set_hour_clicks(120+i)
#     #     await asyncio.sleep(5+i)
#
#     print(await db.get_24_hour_clicks())


# loop = asyncio.get_event_loop()
# loop.run_until_complete(test_hour_clicks_table())