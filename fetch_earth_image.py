import os
import argparse
import requests
from dotenv import load_dotenv
from utils import download_image, get_extension


API_NASA = os.getenv("API_NASA")
IMAGES_DIR = os.path.join(os.getcwd(), "images")
os.makedirs(IMAGES_DIR, exist_ok=True)


def fetch_earth_image(count):

    payload = {
        "api_key": api_key
        }

    url = f'https://api.nasa.gov/EPIC/api/natural/images?api_key={api_key}'
    response = requests.get(url, params=payload)
    response.raise_for_status()

    epic_images = response.json()

    for image_id, latest_image in enumerate(epic_images[:count]):
        latest_image = epic_images[image_id]

        date = latest_image['date']

        image_name = latest_image['image']

        date_part = date.split()[0].split("-")

        year, month , day = date_part

        earth_url = f'https://api.nasa.gov/EPIC/archive/natural/{year}/{month}/{day}/png/{image_name}.png?api_key={api_key}'

        extension = get_extension(earth_url)

        download_image(f"Earth_{year}_{month}_{day}_{image_id + 1}{extension}", earth_url, IMAGES_DIR)


if __name__ == "__main__":
    dotenv_path = os.path.join('secrets.env')
    load_dotenv(dotenv_path=dotenv_path)
    api_key = os.environ['API_EARTH']

    parser = argparse.ArgumentParser(description="Скачивание изображений Земли от NASA")
    parser.add_argument("count", type=int, help="Количество изображений для скачивания", default=1)

    args = parser.parse_args()
    fetch_earth_image(args.count)
