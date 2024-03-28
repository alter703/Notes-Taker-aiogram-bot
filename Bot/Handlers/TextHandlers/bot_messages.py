from aiogram import Router, F
from aiogram.types import Message

from Bot.AdditionalFuncs.presaving_notes import presave_note
from Bot.Keyboards.inline import yesno_save

router = Router()


@router.message(F.text, ~F.text.lower().in_({'delete note by title', 'get note by title'})) # ~(тильда) допомагає ігнорувати вказані речі...
async def ask_set_notes(message: Message):
    await presave_note(user_id=message.from_user.id, text=message.text.capitalize())
    await message.answer('Do you want to save it as note?', reply_markup=yesno_save)
