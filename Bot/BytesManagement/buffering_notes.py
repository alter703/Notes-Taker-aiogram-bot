import asyncio
import aiofiles 
import asyncpg
import os

# from io import BytesIO


async def read_note(buffer):
    buffer.seek(0)
    text_list = buffer.readlines()
    return text_list


async def clear_buffer(buffer):
    buffer.truncate(0)
    buffer.close()
