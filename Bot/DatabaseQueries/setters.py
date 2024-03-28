import asyncpg

from .config_db import USER, DATABASE


async def set_new_note(user_id, title, content) -> None:
    conn = await asyncpg.connect(user=USER, database=DATABASE,
                                  port='5432', host='127.0.0.1',
                                    password='1234')

    try:
        await conn.execute("""
            INSERT INTO notes (user_id, title, content) VALUES ($1, $2, $3);
        """, int(user_id.strip('\n')), str(title.strip('\n')), str(content))
    finally:
        await conn.close()