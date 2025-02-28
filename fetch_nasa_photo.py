import os
import argparse
import requests
from dotenv import load_dotenv
from utils import download_image, get_extension

API_NASA = os.getenv("API_NASA")
IMAGES_DIR = os.path.join(os.getcwd(), "images")

load_dotenv()
os.makedirs(IMAGES_DIR, exist_ok=True)

def fetch_nasa_photo(count):
    url = f'https://api.nasa.gov/planetary/apod?api_key={api_key}'
    payload = {
        "api_key": api_key,
        "count": count
    }

    response = requests.get(url, params=payload)
    response.raise_for_status()

    photos = response.json()

    for photo_id, photo in enumerate(photos, start=1):
        if 'url' in photo:
            link = photo['url']
            extension = get_extension(link)
            download_image(f"Nasa_{id}{extension}", link, IMAGES_DIR)


if __name__ == "__main__":
    dotenv_path = os.path.join('secrets.env')
    load_dotenv(dotenv_path=dotenv_path)
    api_key = os.environ['API_NASA']

    parser = argparse.ArgumentParser(description="Скачивание фотографий NASA")
    parser.add_argument("count", type=int, help="Количество фотографий для скачивания", default=1)

    args = parser.parse_args()
    fetch_nasa_photo(args.count)
