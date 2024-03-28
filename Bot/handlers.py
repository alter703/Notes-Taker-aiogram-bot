import asyncio
import aiogram

from aiogram import Router, F

from aiogram.types import Message, CallbackQuery, BufferedInputFile
from aiogram.filters import CommandStart, Command
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

from .inline_keyboards import yesno, yesno_delete
from .reply_keyboards import get_note_kb

from .BytesNotes.buffering_notes import presave_note, clear_buffer, read_note

from .DatabaseQueries.setters import set_new_note
from .DatabaseQueries.getters import get_all_notes, get_one_note
from .DatabaseQueries.removers import delete_one_note, delete_all_notes

from .DocsNotes.create_docs import create_dock

router = Router()
preview_buffer = None


class ChooseNote(StatesGroup):
    title = State()

class DeleteNote(StatesGroup):
    title = State()

class SendNoteAsDock(StatesGroup):
    title = State()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Hello!', reply_markup=get_note_kb)


@router.message(Command('help'), ~F.text.in_({'get all notes', 'get note by title'}))
async def cmd_start(message: Message):
    await message.answer('I am here!')


@router.message(Command('send_dock'), ~F.text.in_({'get all notes', 'get note by title'}))
async def cmd_start(message: Message, state: FSMContext):
    await state.set_state(SendNoteAsDock.title)
    await message.answer('Type the title to get your note as document (.docx)')


@router.message(Command('delete_all'), ~F.text.in_({'get all notes', 'get note by title'}))
async def cmd_start(message: Message):
    await message.answer('Do You want do delete all your notes? Are you sure? That is irreversable action!', reply_markup=yesno_delete)

@router.message(Command('delete_one'), ~F.text.in_({'get all notes', 'get note by title'}))
async def cmd_start(message: Message, state: FSMContext):
    await state.set_state(DeleteNote.title)
    await message.answer('Type the title to delete your note')


@router.message(F.text.lower().in_({'get all notes', 'get note by title'}))
async def put_notes(message: Message, state: FSMContext):
    if message.text.lower() == 'get all notes':
        rows = await get_all_notes(user_id=message.from_user.id)

        if rows:
            for row in rows:
                await message.answer(f'{row.get('row')[0]}\n\n{row.get('row')[1]}')
                await asyncio.sleep(0.2)
        else:
            await message.answer('You have no any notes in your cloud')

    elif message.text.lower() == 'get note by title':
        await state.set_state(ChooseNote.title)
        await message.answer('Type the title to find your note')


@router.message(ChooseNote.title)
async def find_note(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    try:
        note = await get_one_note(user_id=message.from_user.id, title=message.text)
        await message.answer(''.join(f'*{note[0].get('row')[0]}*\n\n{note[0].get('row')[1]}'))
    except IndexError:
        await message.answer('Sorry, I cannot find this note')

    await state.clear()


@router.message(DeleteNote.title)
async def delete_note(message: Message, state: FSMContext):
    await state.update_data(name=message.text)

    await delete_one_note(user_id=message.chat.id, title=message.text)
    await state.clear()


@router.message(SendNoteAsDock.title)
async def send_document_note(message: Message, state: FSMContext):
    await state.update_data(name=message.text)

    try:
        document = await create_dock(user_id=message.chat.id, title=message.text)
        await message.answer_document(BufferedInputFile(file=document.read(), filename=f'{message.text.replace(' ', '_')[:10]}.docx'))
        document.close()
    except IndexError:
        await message.answer('Sorry, I cannot find this note')

    await state.clear()



@router.message(F.text, ~F.text.lower().in_({'get all notes', 'get note by title'})) # ~(тильда) допомагає ігнорувати вказані речі...
async def ask_set_notes(message: Message):
    global preview_buffer

    preview_buffer = await presave_note(user_id=message.from_user.id, text=message.text)
    await message.answer('Do you want to save it?', reply_markup=yesno)


@router.callback_query(F.data.in_({'do_save', 'do_not_save'}))
async def saving_process(callback: CallbackQuery):
    global preview_buffer
    if callback.data == 'do_save':
        text = await read_note(preview_buffer)
        await set_new_note(user_id=text[0].decode(), title=text[1].decode(), content=''.join(text[2].decode()))
    else:
        await callback.message.answer('Fine')

    await clear_buffer(preview_buffer)


@router.callback_query(F.data.in_({'do_delete', 'do_not_delete'}))
async def saving_process(callback: CallbackQuery):
    if callback.data == 'do_delete':
        await delete_all_notes(user_id=callback.message.chat.id)
        await callback.message.answer('All your notes were deleted!')
    else:
        await callback.message.answer('Maybe you just misclicked the command...')
