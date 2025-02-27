import asyncio
import telegram
from telegram.ext import Application
from config import TELEGRAM_BOT_TOKEN

telegram_app = Application.builder().token(TELEGRAM_BOT_TOKEN).build()



async def main():
    bot = telegram.Bot(TELEGRAM_BOT_TOKEN)
    async with bot:
        await bot.set_webhook("https://telegram-telescope.lukvmil.com/telegram/listener")
        
        # print(updates)
        
if __name__ == '__main__':
    asyncio.run(main())