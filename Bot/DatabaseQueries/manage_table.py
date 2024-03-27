import asyncio
import asyncpg

from .config_db import USER, DATABASE


async def create_table() -> None:
    conn = await asyncpg.connect(user=USER, database=DATABASE,
                                  port='5432', host='127.0.0.1',
                                    password='1234')

    try:
        await conn.execute("""
        CREATE TABLE IF NOT EXISTS notes(
            id SERIAL PRIMARY KEY,
            user_id BIGINT,
            title VARCHAR(255),
            content TEXT
        );

    """)
    finally:
        await conn.close()  
    return


async def drop_table() -> None:
    conn = await asyncpg.connect(user=USER, database=DATABASE,
                                  port='5432', host='127.0.0.1',
                                    password='1234')
    try:
        await conn.execute("""
        DROP TABLE IF EXISTS notes;

    """)
    finally:
        await conn.close()   
    return


if __name__ == '__main__':
    loop = asyncio.new_event_loop()
    loop.run_until_complete(create_table())
