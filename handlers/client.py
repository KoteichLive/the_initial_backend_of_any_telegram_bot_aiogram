from aiogram import types, Dispatcher
from aiogram.types import ContentType


async def voice_message_handler(message):
    if message.content_type == types.ContentType.VOICE:
        pass


async def message_handler(message):
    print(message.text)


def register_client(dp: Dispatcher):
    dp.register_message_handler(message_handler)
    dp.register_message_handler(voice_message_handler, content_types=[ContentType.VOICE])
