import os
import telegram
from dotenv import load_dotenv


dotenv_path = os.path.join('secrets.env')
load_dotenv(dotenv_path=dotenv_path)

api_bot = os.environ['API_TELEBOT']

bot = telegram.Bot(token=api_bot)

chat_id = '@imagensa'

bot.send_photo(chat_id=chat_id, photo=open('images/spacex_2.jpg', 'rb'))
