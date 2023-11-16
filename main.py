import asyncio
from aiogram.filters import Command
from aiogram import Dispatcher, F, types, Bot
from aiogram.enums import ParseMode
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

BOT_TOKEN = "6454202269:AAF0cq_NQswhdJvR8KAncTYHQDOyGes8QHo"
BOT_ID = "6454202269"
CHAT_ID = "353393761"
BOT_NAME = "@aio_my_first_bot"
BOT_LINK = "https://t.me/aio_my_first_bot"


async def set_commands(bot: Bot):
    my_commands = [

    ]

    await bot.set_my_commands([])


def create_my_keyboard():
    my_keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='first', callback_data='in the base1')],
        [InlineKeyboardButton(text='second', callback_data='in the base2')],
    ]
    )
    return my_keyboard


async def start_func(bot: Bot):
    await set_commands(bot)



async def send_dice(message: types.Message):
    await message.bot.send_dice(CHAT_ID, emoji='⚽', reply_markup=create_my_keyboard())


async def process_the_button(call: CallbackQuery):
    await call.answer()






async def main():
    bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.MARKDOWN_V2)
    dispatcher = Dispatcher()

    # handlers and event observers
    dispatcher.startup.register(start_func)
    dispatcher.message.register(send_dice)
    dispatcher.callback_query.register(process_the_button)

    try:
        await dispatcher.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(main())
