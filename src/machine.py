import threading
import asyncio
import time
from lab import telegram, atomspace


tasks = {}


# This is the main loop for the entire machine
@asyncio.coroutine
async def main(loop):
    while True:
        # Prune completed tasks
        for task in tasks.copy():
            if tasks[task].done() or tasks[task].cancelled():
                del tasks[task]

        # Get configs, create tasks, and append to task queue
        if "telegram" not in tasks:
            task = loop.create_task(telegram.subscribe())
            task.set_name("telegram")
            tasks[task.get_name()] = task

        await asyncio.sleep(66.6666)


def loop_in_thread(loop):
    asyncio.set_event_loop(loop)
    loop.run_until_complete(main(loop))


# Start the main loop in a thread
loop = asyncio.get_event_loop()
t = threading.Thread(None, loop_in_thread, args=(loop,), daemon=True)

while True:
    time.sleep(5)
    if not t.is_alive():
        t.start()
