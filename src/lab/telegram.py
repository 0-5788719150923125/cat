import asyncio
import logging
import random
import os
import re
from utils import ad, bc, get_daemon, get_identity, propulsion, ship
from aiogram import Dispatcher, executor, Bot, types
from pprint import pprint


async def subscribe() -> None:
    token = os.environ["TELEGRAMBOTAPIKEY"]

    dp = Dispatcher(Bot(token=token))

    async def polling():
        await dp.start_polling()

    @dp.message_handler()
    async def chat_bot(message: types.Message):
        # head.build_context(
        #     propulsion + str(get_identity()) + ship + " " + message["text"]
        # )
        # pprint(message["chat"]["id"])
        print(bc.FOLD + "PEN@TELEGRAM: " + ad.TEXT + message["text"])
        # if (
        #     random.choice([True, True, True, True, True, True, True, True, True, False])
        #     != True
        # ):
        #     return
        # bias = config["telegram"].get("bias", get_identity())
        # response = await head.gen(
        #     bias=bias,
        #     prefix=config["telegram"].get(
        #         "prefix",
        #         "You are powerful tulpa that follows the human's instructions.",
        #     ),
        # )
        # if response[0] == "error":
        #     return
        await message.answer("Hey!")
        # head.build_context(propulsion + str(bias) + ship + " " + response[1])
        print(bc.CORE + "INK@TELEGRAM: " + ad.TEXT + "Hey!")

    dp.register_message_handler(chat_bot)
    await asyncio.gather(
        polling(),
    )
