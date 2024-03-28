from aiogram.fsm.state import StatesGroup, State


class GetNote(StatesGroup):
    title = State()


class DeleteNote(StatesGroup):
    title = State()


class SendNoteAsDock(StatesGroup):
    title = State()
