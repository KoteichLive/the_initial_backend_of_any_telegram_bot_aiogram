import asyncio

from aiogram.utils import executor

from bor_ import dp
from handlers import client

loop = asyncio.get_event_loop()

print('start')


async def zac():
    pass

client.register_client(dp)


loop.run_until_complete(zac())

if __name__ == '__main__':
    executor.start_polling(dp)
