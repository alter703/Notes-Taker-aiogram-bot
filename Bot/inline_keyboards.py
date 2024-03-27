from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

yesno = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Yes, save it', callback_data='do_save'),
     InlineKeyboardButton(text='No, ignore it', callback_data='do_not_save')]
])


yesno_delete = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Yes, delete all', callback_data='do_delete'),
     InlineKeyboardButton(text='No, ignore it', callback_data='do_not_delete')]
])
