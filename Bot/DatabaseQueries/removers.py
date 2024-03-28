import asyncpg

from .config_db import USER, DATABASE


async def delete_one_note(user_id, title) -> None:
    conn = await asyncpg.connect(user=USER, database=DATABASE,
                                  port='5432', host='127.0.0.1',
                                    password='1234')
    # print(title, user_id)
    try:
        await conn.execute("""
            DELETE FROM notes WHERE user_id = $1 AND title = $2;
        """, int(user_id), str(title.strip('\n')))
    finally:
        await conn.close()

async def delete_all_notes(user_id) -> None:
    conn = await asyncpg.connect(user=USER, database=DATABASE,
                                  port='5432', host='127.0.0.1',
                                    password='1234')
    # print(user_id)
    try:
        await conn.execute("""
            DELETE FROM notes WHERE user_id = $1;
        """, int(user_id))
    finally:
        await conn.close()
