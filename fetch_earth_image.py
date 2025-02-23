import os
import argparse
import requests
from dotenv import load_dotenv
from utils import download_image, check_extension

API_NASA = os.getenv("API_NASA")
IMAGES_DIR = os.path.join(os.getcwd(), "images")

load_dotenv()
os.makedirs(IMAGES_DIR, exist_ok=True)

def fetch_earth_image(count):
    dotenv_path = os.path.join('secrets.env')
    load_dotenv(dotenv_path=dotenv_path)
    api_key = os.environ['API_EARTH'] 

    url = f'https://api.nasa.gov/EPIC/api/natural/images?api_key={api_key}'
    response = requests.get(url)
    response.raise_for_status()

    images_data = response.json()

    for image_id in range(count):
        latest_image = images_data[image_id]

        date = latest_image['date']

        image_name = latest_image['image']

        date_part = date.split()[0].split("-")

        year, month , day = date_part

        earth_url = f'https://api.nasa.gov/EPIC/archive/natural/{year}/{month}/{day}/png/{image_name}.png?api_key={api_key}'

        extension = check_extension(earth_url)

        download_image(f"Earth_{year}_{month}_{day}_{image_id + 1}{extension}", earth_url, IMAGES_DIR)


def main():
    parser = argparse.ArgumentParser(description="Скачивание изображений Земли от NASA")
    parser.add_argument("count", type=int, help="Количество изображений для скачивания", default=1)

    args = parser.parse_args()
    fetch_earth_image(args.count)

if __name__ == "__main__":
    main()