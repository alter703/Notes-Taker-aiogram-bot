import asyncio

from aiogram import Router, F

from aiogram.types import Message, BufferedInputFile
from aiogram.fsm.context import FSMContext

from Bot.States.states import SendNoteAsDock, GetNote, DeleteNote
from Bot.DatabaseQueries.getters import get_one_note
from Bot.DatabaseQueries.removers import delete_one_note
from Bot.DocsNotes.create_docs import create_dock

from Bot.BytesManagement.buffering_notes import clear_buffer

router = Router()


@router.message(GetNote.title)
async def find_note(message: Message, state: FSMContext):
    await state.update_data(name=message.text)

    try:
        note = await get_one_note(user_id=message.from_user.id, title=message.text.capitalize())
        await message.answer(''.join(f'*{note[0].get('row')[0]}*\n\n{note[0].get('row')[1]}'))
    except IndexError:
        await message.answer('Sorry, I cannot find this note')

    await state.clear()


@router.message(DeleteNote.title)
async def delete_note(message: Message, state: FSMContext):
    await state.update_data(name=message.text)

    await delete_one_note(user_id=message.chat.id, title=message.text.capitalize())
    await message.answer(f'Your note {message.text} is delete!')
    await state.clear()


@router.message(SendNoteAsDock.title)
async def send_document_note(message: Message, state: FSMContext):
    await state.update_data(name=message.text)

    try:
        document = await create_dock(user_id=message.chat.id, title=message.text.capitalize())
        await message.answer_document(BufferedInputFile(file=document.read(), filename=f'{message.text.capitalize().replace(' ', '_')[:10]}.docx'))
        clear_buffer(document)
        document.close()
    except IndexError:
        await message.answer('Sorry, I cannot find this note')

    await state.clear()
