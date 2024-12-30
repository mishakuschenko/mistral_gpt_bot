from aiogram import Router, F
from aiogram.types import Message 
from aiogram.filters import CommandStart, Command

from config import models
from config import ai_token

from mistralai import Mistral 

rt: Router = Router()
client = Mistral(api_key=ai_token)


@rt.message(CommandStart())
async def cmd_start(msg: Message) -> None:
    await msg.answer("Привет! Напиши что нибудь!\nПроблемы ➡️ /help")


@rt.message(Command("help"))
async def help(msg: Message) -> None:
    await msg.answer("По любым вопросам обращайтесь сюда ➡️ https://t.me/nameofaccaunt ")


@rt.message(F.text) 
async def gen(msg: Message) -> None:

    wait_message = await msg.answer("Готовлю ответ...")

    response = client.chat.complete(
        model = models["ministral-8b-latest"], 
        messages = [
            {
                "role": "user",
                "content": f"{msg.text}",  
            },
        ],
    )
    
    await msg.bot.delete_message(chat_id=msg.chat.id, message_id=wait_message.message_id)
    await msg.answer(response.choices[0].message.content, parse_mode = "Markdown")

