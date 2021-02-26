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
