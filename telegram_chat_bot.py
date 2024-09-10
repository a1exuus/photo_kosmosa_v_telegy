import telegram
from dotenv import load_dotenv
import os

load_dotenv()

bot_token = os.getenv('TG_BOT_TOKEN')
bot = telegram.Bot(token=bot_token)
chat_id = '-1002265052157'
bot.send_message(chat_id=chat_id, text='Привет, салам алейкум лееееееееееее')