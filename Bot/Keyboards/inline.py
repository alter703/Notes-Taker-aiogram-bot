from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


yesno_save = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Yes, save it', callback_data='do_save'),
     InlineKeyboardButton(text='No, ignore it', callback_data='do_not_save')]
])


yesno_delete = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Yes, delete all', callback_data='do_delete_all'),
     InlineKeyboardButton(text='No, ignore it', callback_data='do_not_delete_all')]
])
