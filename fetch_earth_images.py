import os
import argparse
import requests
from dotenv import load_dotenv
from utils import download_image, get_extension
from urllib.parse import urlencode

def fetch_earth_images(count):

    payload = {
        "api_key": api_key_earth
    }

    url = f'https://api.nasa.gov/EPIC/api/natural/images'
    response = requests.get(url, params=payload)
    response.raise_for_status()
    epic_images = response.json()

    for image_id, latest_image in enumerate(epic_images[:count], start=1):

        latest_image = epic_images[image_id]
        date = latest_image['date']
        image_name = latest_image['image']
        date_part = date.split()[0].split("-")
        year, month , day = date_part
        earth_url = f'https://api.nasa.gov/EPIC/archive/natural/{year}/{month}/{day}/png/{image_name}.png'
        extension = get_extension(earth_url)

        download_image(f"Earth_{year}_{month}_{day}_{image_id}{extension}", earth_url, images_dir, params=payload)


if __name__ == "__main__":
    images_dir = os.path.join(os.getcwd(), "images")
    os.makedirs(images_dir, exist_ok=True)

    dotenv_path = os.path.join('secrets.env')
    load_dotenv(dotenv_path=dotenv_path)
    api_key_earth = os.environ['API_KEY_EARTH']

    parser = argparse.ArgumentParser(description="Скачивание изображений Земли от NASA")
    parser.add_argument("count", type=int, help="Количество изображений для скачивания", default=1)

    args = parser.parse_args()
    fetch_earth_images(args.count)
