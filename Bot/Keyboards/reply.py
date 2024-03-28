from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder


note_options = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Get note by title'),
     KeyboardButton(text='Delete note by title')]
],
resize_keyboard=True)
