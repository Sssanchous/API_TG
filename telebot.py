import os
import telegram
from dotenv import load_dotenv
import random
import time
import argparse


def collect_image_files():
    files = []
    for root, dirs, files in os.walk('images'):
        files.extend(files)
    return files


def publish_images(chat_id):
    delay = int(os.getenv('PUBLISH_DELAY_HOURS')) * 3600
    while True:
        files = collect_image_files()

        random.shuffle(files)

        for file in files:
            file_path = os.path.join('images', file)
            if os.path.exists(file_path):  
                with open(file_path, 'rb') as photo:
                    bot.send_photo(chat_id=chat_id, photo=photo)
                time.sleep(delay)

def publish_delay_hours():
    delay = int(os.getenv('PUBLISH_DELAY_HOURS'))
    return delay * 3600


if __name__ == '__main__':

    dotenv_path = os.path.join('secrets.env')
    load_dotenv(dotenv_path=dotenv_path)
    api_key_telebot  = os.environ['API_KEY_BOT']
    bot = telegram.Bot(token=api_key_telebot)
    publish_delay_hours()
    chat_id = os.environ.get('CHAT_ID')

    publish_images(chat_id)