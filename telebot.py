import os
import telegram
from dotenv import load_dotenv
import random
import time
import argparse


def takefiles():
    files = []
    for root, dirs, files in os.walk('images'):
        files.extend(files)
    return files


def publish_images(chat_id):
    delay = int(os.getenv('PUBLISH_DELAY_HOURS')) * 3600
    while True:
        files = takefiles()

        random.shuffle(files)

        for file in files:
            file_path = os.path.join('images', file)
            if os.path.exists(file_path):  
                with open(file_path, 'rb') as photo:
                    bot.send_photo(chat_id=chat_id, photo=photo)
                time.sleep(delay)



if __name__ == '__main__':

    dotenv_path = os.path.join('secrets.env')
    load_dotenv(dotenv_path=dotenv_path)
    api_bot = os.environ['API_TELEBOT']
    bot = telegram.Bot(token=api_bot)
    delay = int(os.getenv('PUBLISH_DELAY_HOURS')) * 3600

    parser = argparse.ArgumentParser(description="Публикация изображений в Telegram")
    parser.add_argument('chat_id')
    args = parser.parse_args()

    chat_id = args.chat_id

    publish_images(chat_id)