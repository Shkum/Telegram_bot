from aiogram.utils import executor
from create_bot import dp


async def on_startup(_):
    print('Bot is online...')

from handlers import client, admin, other

client.register_handlers_client(dp)
other.register_handles_other(dp)

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
