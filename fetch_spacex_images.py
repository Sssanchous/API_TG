import os
import argparse
import requests
from utils import download_image


def fetch_spacex_last_launch(id_last_launch):

    url = f'https://api.spacexdata.com/v5/launches/{id_last_launch}'
    response = requests.get(url)
    response.raise_for_status()

    launches = response.json()
    image_urls = launches["links"]["flickr"]["original"]

    for link_id, link in enumerate(image_urls, start=1):
        download_image(f"spacex_{id}.jpg", link, images_dir)


if __name__ == "__main__":
    images_dir  = os.path.join(os.getcwd(), "images")
    os.makedirs(images_dir, exist_ok=True)

    parser = argparse.ArgumentParser(description="Скачивание фотографий SpaceX")
    parser.add_argument("id_last_launch", help="ID запуска SpaceX (по умолчанию – последний запуск)", nargs="?", default='latest')

    args = parser.parse_args()
    fetch_spacex_last_launch(args.id_last_launch)
