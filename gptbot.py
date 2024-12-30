from mistralai import Mistral 

from aiogram import Bot, Dispatcher, Router
from aiogram.types import Message 
from aiogram.filters import CommandStart, Command

from config import token 
from config import ai_token

import asyncio

rt: Router = Router()
client = Mistral(api_key=ai_token)


@rt.message(CommandStart())
async def cmd_start(msg: Message) -> None:
    await msg.answer("Привет! Напиши что нибудь!\nПроблемы ➡️ /help")


@rt.message(Command("help"))
async def help(msg: Message) -> None:
    await msg.answer("По любым вопросам обращайтесь сюда ➡️ https://t.me/nameofaccaunt ")


@rt.message()
async def gen(msg: Message) -> None:

    wait_message = await msg.answer("Готовлю ответ...")

    response = client.chat.complete(
        model='mistral-small-latest', 
        messages = [
            {
                "role": "user",
                "content": f"{msg.text}",  
            },
        ],
    )
    await msg.bot.delete_message(chat_id=msg.chat.id, message_id=wait_message.message_id)
    await msg.answer(response.choices[0].message.content, parse_mode = "Markdown")


async def main() -> None:
    bot = Bot(token=token)
    dp = Dispatcher()
    dp.include_router(rt)
    await dp.start_polling(bot)


if __name__ == '__main__':
    print("Start!")
    asyncio.run(main())

