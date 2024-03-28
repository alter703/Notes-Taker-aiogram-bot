from aiogram import Router, F

from aiogram.types import CallbackQuery
from Bot.DatabaseQueries.removers import delete_all_notes
from Bot.AdditionalFuncs.presaving_notes import read_text_and_save

router = Router()


@router.callback_query(F.data.in_({'do_save', 'do_not_save'}))
async def saving_process(callback: CallbackQuery):
    text = await read_text_and_save(callback.message.chat.id)
    if callback.data == 'do_save':
        await callback.message.answer(f'Your note {text[1]} is saved!')
    else:
        await callback.message.answer('Fine')


@router.callback_query(F.data.in_({'do_delete_all', 'do_not_delete_all'}))
async def saving_process(callback: CallbackQuery):
    if callback.data == 'do_delete_all':
        await delete_all_notes(user_id=callback.message.chat.id)
        await callback.message.answer('All your notes were deleted!')
    else:
        await callback.message.answer('Maybe you just misclicked the command...')
