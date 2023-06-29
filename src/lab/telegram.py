import asyncio
import logging
import random
import os
import subprocess
import shlex
import re
from utils import ad, bc, get_daemon, get_identity, propulsion, ship
from aiogram import Dispatcher, executor, Bot, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from lab.atomspace import put_atom, get_atom, get_atom_by_name


logging.basicConfig(level=logging.INFO)

storage = MemoryStorage()


# States
class Form(StatesGroup):
    name = State()  # Will be represented in storage as 'Form:name'
    # age = State()  # Will be represented in storage as 'Form:age'
    # gender = State()  # Will be represented in storage as 'Form:gender'


async def subscribe() -> None:
    token = os.environ["TELEGRAMBOTAPIKEY"]

    dp = Dispatcher(Bot(token=token), storage=storage)

    print("starting telegram bot")

    async def polling():
        await dp.start_polling()

    # You can use state '*' if you need to handle all states
    @dp.message_handler(state="*", commands="cancel")
    @dp.message_handler(Text(equals="cancel", ignore_case=True), state="*")
    async def cancel_handler(message: types.Message, state: FSMContext):
        """
        Allow user to cancel any action
        """
        current_state = await state.get_state()

        if current_state is None:
            return

        logging.info("Cancelling state %r", current_state)
        # Cancel state and inform user about it
        await state.finish()
        await message.reply("Cancelled.", reply_markup=types.ReplyKeyboardRemove())

    @dp.message_handler(commands=["atom"])
    async def get_atom(message: types.Message):
        """
        This handler will be called when user sends `/start` or `/help` command
        """
        print(message.text)
        # result = get_atom_by_name("atom1")
        # print(result)
        await Form.name.set()
        await message.reply("Which atom shall I focus on?")

    @dp.message_handler(state=Form.name)
    async def process_name(message: types.Message, state: FSMContext):
        """
        Process user name
        """
        print(message.text)
        async with state.proxy() as data:
            data["name"] = message.text

        # await Form.next()
        # await message.reply("How old are you?")
        await state.finish()

    @dp.message_handler()
    async def chat_bot(message: types.Message):
        print(bc.FOLD + "YOU@TELEGRAM: " + ad.TEXT + message["text"])
        try:
            args = shlex.split(message["text"])
            output = subprocess.run(
                args, capture_output=True, text=True, check=True
            ).stdout
        except Exception as e:
            output = e
        await message.answer(str(output))

    await asyncio.gather(
        polling(),
    )
