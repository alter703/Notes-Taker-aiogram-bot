from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

get_note_kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Get all notes'),
     KeyboardButton(text='Get note by title')]
],
resize_keyboard=True)
