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


def publish_images(bot, chat_id, delay_hours):
    while True:
        files = collect_image_files()

        random.shuffle(files)

        for file in files:
            file_path = os.path.join('images', file)
            if os.path.exists(file_path):  
                with open(file_path, 'rb') as photo:
                    bot.send_photo(chat_id=chat_id, photo=photo)
                time.sleep(delay_hours)


if __name__ == '__main__':

    dotenv_path = os.path.join('secrets.env')
    load_dotenv(dotenv_path=dotenv_path)
    api_key_telebot  = os.environ['API_KEY_BOT']
    bot = telegram.Bot(token=api_key_telebot)
    chat_id = os.environ.get('TG_CHAT_ID')
    delay_hours = int(os.getenv('PUBLISH_DELAY_HOURS', 4)) * 3600

    publish_images(bot, chat_id, delay_hours)