import os
import argparse
import requests
from dotenv import load_dotenv
from utils import download_image, get_extension


def fetch_nasa_photos(count):
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
            download_image(f"Nasa_{photo_id}{extension}", link, images_dir)


if __name__ == "__main__":
    images_dir = os.path.join(os.getcwd(), "images")
    os.makedirs(images_dir, exist_ok=True)

    dotenv_path = os.path.join('secrets.env')
    load_dotenv(dotenv_path=dotenv_path)
    api_key = os.environ['API_NASA']

    parser = argparse.ArgumentParser(description="Скачивание фотографий NASA")
    parser.add_argument("count", type=int, help="Количество фотографий для скачивания", default=1)

    args = parser.parse_args()
    fetch_nasa_photos(args.count)
