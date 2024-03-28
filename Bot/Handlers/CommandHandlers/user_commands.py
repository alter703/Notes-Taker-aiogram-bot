import asyncio

from aiogram import Router, F

from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext

from Bot.States.states import SendNoteAsDock
from Bot.DatabaseQueries.getters import get_all_notes

from Bot.Keyboards.reply import note_options
from Bot.Keyboards.inline import yesno_delete

router = Router()


@router.message(CommandStart())
async def start_chat(message: Message):
    await message.answer('Hello!', reply_markup=note_options)


@router.message(Command('help'))
async def help_command(message: Message):
    await message.answer('I am here!')


@router.message(Command('get_dock'))
async def ask_title_to_put_dock(message: Message, state: FSMContext):
    await state.set_state(SendNoteAsDock.title)
    await message.answer('Type the title to get your note as document (.docx)')


@router.message(Command('delete_all'))
async def delete_all(message: Message):
    await message.answer('Do You want do delete all your notes? Are you sure? That is irreversable action!', reply_markup=yesno_delete)


@router.message(Command('get_all'))
async def get_all(message: Message):
    rows = await get_all_notes(user_id=message.from_user.id)

    if rows:
        for index_row, row in enumerate(rows, start=1):
            await message.answer(f'*{index_row}.{row.get('row')[0]}*\n\n{row.get('row')[1]}')
            await asyncio.sleep(0.2)
    else:
        await message.answer('You have no any notes in your cloud')    
