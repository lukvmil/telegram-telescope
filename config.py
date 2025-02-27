from dotenv import load_dotenv
import os
from datetime import timedelta
load_dotenv()

DEBUG = os.path.exists("app/debug")
print("DEBUG MODE:", DEBUG)

TELEGRAM_BOT_TOKEN=os.environ["TELEGRAM_BOT_TOKEN"]