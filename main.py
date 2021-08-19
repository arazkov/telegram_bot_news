import asyncio
import logging
from aiogram import Bot, Dispatcher, executor, types
from pars import get_last_articles

API_TOKEN = ''
user_id = 1455367819

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)


async def send_new_articles():
    while True:
        last = get_last_articles()
        if last:
            for article in last.values():
                my_answer = f"<b>{article['name']}</b>\n<i>{article['date']}</i>\n{article['anotation']}\n{article['url']}"
                await bot.send_photo(user_id, article['img'], my_answer)
        await asyncio.sleep(3600) #repeat every hour


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(send_new_articles())
    executor.start_polling(dp, skip_updates=True)

