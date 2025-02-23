import os
import telegram
from dotenv import load_dotenv
import random
import time

dotenv_path = os.path.join('secrets.env')
load_dotenv(dotenv_path=dotenv_path)
api_bot = os.environ['API_TELEBOT']

bot = telegram.Bot(token=api_bot)

chat_id = '@imagensa'


def takeFiles():
    files = []
    for root, dirs, files in os.walk('images'):
        files.append(files)
    return files


def publish_images():
    delay = int(os.getenv('PUBLISH_DELAY_HOURS')) * 3600
    while True:
        files = takeFiles()

        random.shuffle(files)

        for file in files:
            bot.send_photo(chat_id=chat_id, photo=open(f'images/{file}', 'rb'))
            time.sleep(delay)

if __name__ == '__main__':
    publish_images()