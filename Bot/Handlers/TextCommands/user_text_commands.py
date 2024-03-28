from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from Bot.Handlers.StateHandlers.state_messages import GetNote, DeleteNote

router = Router()


@router.message(F.text.lower() == 'get note by title') # ~(тильда) допомагає ігнорувати вказані речі...
async def ask_title_to_get_note(message: Message, state: FSMContext):
    await state.set_state(GetNote.title)
    await message.answer('Type the title to get your note')


@router.message(F.text.lower() == 'delete note by title') # ~(тильда) допомагає ігнорувати вказані речі...
async def ask_title_to_delete_note(message: Message, state: FSMContext):
    await state.set_state(DeleteNote.title)
    await message.answer('Type the title to delete your note')
