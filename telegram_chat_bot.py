import telegram
from dotenv import load_dotenv
import os

load_dotenv()

bot_token = os.getenv('TG_BOT_TOKEN')
bot = telegram.Bot(token=bot_token)
chat_id = '-1002265052157'
bot.send_document(chat_id=chat_id, document=open('image/nasa_apod_0.png', 'rb'))