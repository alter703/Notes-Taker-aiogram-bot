import asyncio
import logging

from aiogram import Bot, Dispatcher

from Bot.config import _TOKEN
from Bot.handlers import router


bot = Bot(_TOKEN, parse_mode='markdown')
dp = Dispatcher()


async def main():
    dp.include_router(router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(levelname)s:%(asctime)s:%(message)s')
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Bot is stopped')
