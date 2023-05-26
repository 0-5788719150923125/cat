import asyncio
import logging
import random
import os
import re
from utils import ad, bc, get_daemon, get_identity, propulsion, ship
from aiogram import Dispatcher, executor, Bot, types
from lab.atomspace import put_atom, get_atom


async def subscribe() -> None:
    token = os.environ["TELEGRAMBOTAPIKEY"]

    dp = Dispatcher(Bot(token=token))

    async def polling():
        await dp.start_polling()

    @dp.message_handler()
    async def chat_bot(message: types.Message):
        atom = put_atom(message["text"])
        print(bc.FOLD + "YOU@TELEGRAM: " + ad.TEXT + message["text"])
        # await message.answer(atom.name)
        # print(bc.CORE + "EVE@TELEGRAM: " + ad.TEXT + atom.long_string())
        # print(atom.tv)

    dp.register_message_handler(chat_bot)
    await asyncio.gather(
        polling(),
    )
