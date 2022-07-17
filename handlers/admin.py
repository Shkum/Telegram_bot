# from aiogram import Bot, types
# from aiogram.dispatcher import Dispatcher
# from aiogram.utils import executor
#
# import os, json, string
#
# bot = Bot(token=os.getenv('TOKEN'))
# dp = Dispatcher(bot)
#
#
# async def on_startup(_):
#     print('Bot is online...')
#
#
# '''****************************CLIENT PART*********************************************'''
#
#
# @dp.message_handler(commands=['start', 'help'])
# async def command_start(message: types.message):
#     try:
#         await bot.send_message(message.from_user.id, 'Hello')
#         await message.delete()
#     except:
#         await message.reply('Sent private message to bot: \nhttp://t.me/Raininformer')
#
#
# @dp.message_handler(commands=['work_schedule'])
# async def schedule(message: types.message):
#     await bot.send_message(message.from_user.id, '24 hrs per day')
#
#
# @dp.message_handler(commands=['location'])
# async def schedule(message: types.message):
#     await bot.send_message(message.from_user.id, 'current location:')
#
#
# '''****************************ADMIN PART**********************************************'''
#
# '''****************************GENERAL PART********************************************'''
#
#
# @dp.message_handler()
# async def echo_send(message: types.Message):
#     # if message.text == 'Hi':
#     #     await message.answer('Hallo')
#     # # # await message.answer(message.text) # Just reply
#     # # # await message.reply(message.text) # reply including message to reply
#     # # await bot.send_message(message.from_user.id, message.text) # reply private message
#     if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split(' ')}.intersection(set(json.load(open('cenz.json')))) != set():
#         await message.reply('No bad words')
#         await message.delete()
#
#
# executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
