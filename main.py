from aiogram import Bot, Dispatcher

import mistralai

import asyncio

from handlers import rt 

from config import token

async def main() -> None:
    bot = Bot(token=token)
    dp = Dispatcher()
    dp.include_router(rt)
    await dp.start_polling(bot)


if __name__ == '__main__':
    #models = mistralai.models()
    #for model in models:
    #    print(model)
    print("Start!")
    asyncio.run(main())

