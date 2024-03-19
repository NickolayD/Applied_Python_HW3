import pytest
from aiogram.filters import Command
from aiogram_tests import MockedBot
from aiogram_tests.handler import MessageHandler
from aiogram_tests.types.dataset import MESSAGE
from bot import command_handler
from bot import echo_handler


@pytest.mark.asyncio
async def test_message_handler():
    requester = MockedBot(MessageHandler(echo_handler))
    calls = await requester.query(MESSAGE.as_object(text="Hello!"))
    answer_message = calls.send_message.fetchone().text
    assert answer_message == "Hello!"


@pytest.mark.asyncio
async def test_command_handler():
    requester = MockedBot(MessageHandler(command_handler,
                                         Command(commands=["start"])
                                         )
                          )
    calls = await requester.query(MESSAGE.as_object(text="/start"))
    answer_message = calls.send_message.fetchone().text
    assert answer_message == "Hello, new user!"
