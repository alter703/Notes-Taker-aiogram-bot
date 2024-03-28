import asyncio
import aiofiles 
import asyncpg
import os

from io import BytesIO

from Bot.DatabaseQueries.setters import set_new_note


async def presave_note2(user_id, text):
    title = text.split('.')[0]
    whole_text = f"{user_id}\n{title}\n{text}"

    preview_path_folder = 'temp_files'

    if not os.path.exists(preview_path_folder):
        os.mkdir(preview_path_folder)

    async with aiofiles.open(f'{preview_path_folder}/pn{user_id}.txt', 'w', encoding='utf-8') as preview_file:
        await preview_file.write(whole_text)


async def read_text_and_save(user_id):
    path_preview_file = f'temp_files/pn{user_id}.txt'
    async with aiofiles.open(path_preview_file, 'r', encoding='utf-8') as preview_file:
        text = await preview_file.readlines()

    await set_new_note(user_id=text[0], title=text[1], content=''.join(text[2:]))
    os.remove(path_preview_file)

    return text


async def presave_note(user_id, text):
    title = text.split('.')[0]

    whole_text = f"{user_id}\n{title}\n{text}"

    buf = BytesIO()
    buf.write(whole_text.encode() + b"\n")
    buf.seek(0)  # Переміщаємо курсор на початок потоку
    return buf


async def read_note(buffer):
    buffer.seek(0)
    text_list = buffer.readlines()
    return text_list


async def clear_buffer(buffer):
    buffer.truncate(0)
    buffer.close()


if __name__ == '__main__':
    r = asyncio.run(read_note('#buffer'))
    print(r)