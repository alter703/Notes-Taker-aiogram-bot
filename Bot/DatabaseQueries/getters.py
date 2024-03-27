import asyncpg

from .config_db import USER, DATABASE


async def get_all_notes(user_id):
    conn = await asyncpg.connect(user=USER, database=DATABASE,
                                  port='5432', host='127.0.0.1',
                                    password='1234')
    try:
        all_notes = await conn.fetch("""
        SELECT (title, content) FROM notes WHERE user_id = $1; 

    """, user_id)
    finally:
        await conn.close()
    return all_notes


async def get_one_note(user_id, title):
    conn = await asyncpg.connect(user=USER, database=DATABASE,
                                  port='5432', host='127.0.0.1',
                                    password='1234')
    # try:
    one_note = await conn.fetchrow("""
    SELECT (title, content) FROM notes WHERE user_id = $1 AND title = $2;

    """, user_id, title)
    # finally:
    await conn.close()
    return one_note


async def get_note_as_docx(user_id):
    conn = await asyncpg.connect(user=USER, database=DATABASE,
                                  port='5432', host='127.0.0.1',
                                    password='1234')
    try:
        one_note = await conn.fetch("""
        SELECT note FROM notes WHERE user_id = $1;

    """, user_id)
    finally:
        await conn.close()
    return one_note