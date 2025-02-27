import asyncio
import telegram
from telegram.ext import Application
from .config import TELEGRAM_BOT_TOKEN

telegram_app = Application.builder().token(TELEGRAM_BOT_TOKEN).build()



async def main():
    bot = telegram.Bot()
    async with bot:
        update = (await bot.get_updates(timeout=10))[0]
        chat_id = update.message.chat.id
        await bot.send_message(chat_id, "hello!")
        # breakpoint()
        # print(updates)
        
if __name__ == '__main__':
    asyncio.run(main())