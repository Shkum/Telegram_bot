from aiogram import types, Dispatcher
import json, string
from create_bot import dp


#@dp.message_handler()
async def echo_send(message: types.Message):
    # if message.text == 'Hi':
    #     await message.answer('Hallo')
    # # # await message.answer(message.text) # Just reply
    # # # await message.reply(message.text) # reply including message to reply
    # # await bot.send_message(message.from_user.id, message.text) # reply private message
    if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split(' ')}.intersection(set(json.load(open('cenz.json')))) != set():
        await message.reply('No bad words')
        await message.delete()


def register_handles_other(dp: Dispatcher):
    dp.register_message_handler(echo_send)
