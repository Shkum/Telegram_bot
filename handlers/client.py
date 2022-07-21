from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_client
from aiogram.types import ReplyKeyboardRemove


# @dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.message):
    try:
        await bot.send_message(message.from_user.id, "Hello, let's start", reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply('Sent private message to bot: \nhttp://t.me/Raininformer')


# @dp.message_handler(commands=['Schedule'])
async def schedule(message: types.message):
    await bot.send_message(message.from_user.id, '24 hrs per day')


# @dp.message_handler(commands=['Location'])
async def location(message: types.message):
    await bot.send_message(message.from_user.id, 'current location:')  # reply_markup=ReplyKeyboardRemove()) # remove keyboard after use


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(schedule, commands=['schedule'])
    dp.register_message_handler(location, commands=['location'])
