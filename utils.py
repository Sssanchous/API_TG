import requests
import os
from urllib.parse import urlsplit, unquote


def download_image(filename, url, folder):

    file_path = os.path.join(folder, filename)
    response = requests.get(url)
    response.raise_for_status()

    with open(file_path, 'wb') as file:
        file.write(response.content)


def get_extension(url):

    url_split = urlsplit(url)
    url_unquote = unquote(url_split.path)
    filename, extension = os.path.splitext(url_unquote.strip())

    return extension
