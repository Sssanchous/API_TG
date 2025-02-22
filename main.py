import requests
import os
from dotenv import load_dotenv
from urllib.parse import urlsplit, unquote


images_dir = os.path.join(os.getcwd(), "images")

os.makedirs(images_dir, exist_ok=True)


def download_image(filename, url, folder):

    file_path = os.path.join(folder, filename)

    response = requests.get(url)
    response.raise_for_status()

    with open(file_path, 'wb') as file:
        file.write(response.content)


def check_extension(url):

    split_url= urlsplit(url)

    url_unquote = unquote(url_split.path)

    filename, extension = os.path.splitext(url_unquote.strip())

    return extension


def fetch_spacex_last_launch(id_last_launch):

    url = f'https://api.spacexdata.com/v5/launches/{id_last_launch}'
    response = requests.get(url)
    response.raise_for_status()

    launches = response.json()
    data = launches["links"]["flickr"]["original"]

    for id, link in enumerate(data, start=1):
        download_image(f"spacex_{id}.jpg", link, images_dir)

# fetch_spacex_last_launch('5eb87d47ffd86e000604b38a')

def fetch_nasa_photo(count):

    dotenv_path = os.path.join('secrets.env')
    load_dotenv(dotenv_path=dotenv_path)
    api_key = os.environ['API_NASA']

    url = f'https://api.nasa.gov/planetary/apod?api_key={api_key}'
    payload ={
        "api_key": api_key,
        "count": count
    }

    response = requests.get(url, params=payload)
    response.raise_for_status()

    photos = response.json()

    for id, photo in enumerate(photos, start=1):
        if 'url' in photo:
            link = photo['url']
            extension = check_extension(link)
            download_image(f"Nasa_{id}{extension}", link, images_dir)


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

        download_image(f"Earth_{year}_{month}_{day}_{image_id + 1}{extension}", earth_url, images_dir)


fetch_earth_image(2)
