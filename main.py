import asyncio
import logging

from aiogram import Bot, Dispatcher

from Bot.config import _TOKEN

from Bot.Handlers.CommandHandlers import user_commands
from Bot.Handlers.StateHandlers import state_messages
from Bot.Handlers.TextCommands import user_text_commands
from Bot.Handlers.TextHandlers import bot_messages

from Bot.Callbacks import user_callbacks


bot = Bot(_TOKEN, parse_mode='markdown')
dp = Dispatcher()


async def main():
    dp.include_routers(
        user_commands.router,
        user_text_commands.router,
        state_messages.router,
        bot_messages.router,
        user_callbacks.router
    )
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(levelname)s:%(asctime)s:%(message)s')
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Bot is stopped')
