import aiofiles
import os

from Bot.DatabaseQueries.setters import set_new_note

PREVIEW_FOLDER_PATH = 'temp_files'


async def presave_note(user_id, text):
    global PREVIEW_FOLDER_PATH

    title = text.split('.')[0].strip()
    whole_text = f"{user_id}\n{title}\n{text}"

    if not os.path.exists(PREVIEW_FOLDER_PATH):
        os.mkdir(PREVIEW_FOLDER_PATH)

    async with aiofiles.open(f'{PREVIEW_FOLDER_PATH}/pn{user_id}.txt', 'w', encoding='utf-8') as preview_file:
        await preview_file.write(whole_text)


async def read_text_and_save(user_id):
    path_preview_file = f'{PREVIEW_FOLDER_PATH}/pn{user_id}.txt'

    async with aiofiles.open(path_preview_file, 'r', encoding='utf-8') as preview_file:
        text = await preview_file.readlines()

    await set_new_note(user_id=text[0], title=text[1], content=''.join(text[2:]))
    os.remove(path_preview_file)

    return text
