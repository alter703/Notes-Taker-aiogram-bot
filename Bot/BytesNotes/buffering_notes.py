import asyncio

from io import BytesIO


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
    print(read_note())