import requests
import json
from dotenv import load_dotenv
import os
from urllib.parse import urlsplit, unquote
import io
import datetime

load_dotenv()
nasa_api_key = os.getenv("NASA_API_KEY")
os.makedirs('image', exist_ok=True)


def save_picture(url, api_key, count):
    params = {
        'api_key': api_key,
        'count': count
     }
    response = requests.get(url, params=params)
    jsonq = json.loads(response.text)
    response.raise_for_status()
    for index, image_json in enumerate(jsonq):
        if 'url' in image_json:
            path = f'image/nasa_apod_{index}.png'
            image_url = image_json['url']
            response = requests.get(image_url)
            with open(path, 'wb') as file:
                file.write(response.content)
        else:
            path = f'image/nasa_epic_{index}.png'
            link_epic_archive = 'https://api.nasa.gov/EPIC/archive/natural'
            image_id = image_json['image']
            image_date = datetime.datetime.fromisoformat(image_json['date'])
            parsed_image_date = image_date.strftime('%Y/%m/%d')
            url_a = f'{link_epic_archive}/{parsed_image_date}/png/{image_id}.png'
            response = requests.get(url_a, params=params)
            with io.open(path, 'wb') as file:
                file.write(response.content)



def save_apod_picture(url, api_key, count):
    params = {
        'api_key': api_key,
        'count': count
     }
    response = requests.get(url, params=params)
    jsonq = json.loads(response.text)
    response.raise_for_status()
    for index, image_json in enumerate(jsonq):
        path = f'image/nasa_apod_{index}.png'
        image_url = image_json['url']
        response = requests.get(image_url)
        with open(path, 'wb') as file:
            file.write(response.content)


def get_file_extension(image_link):
    deciphered_image_link = unquote(image_link)
    link_urlsplit = urlsplit(deciphered_image_link).path
    file_name = os.path.split(link_urlsplit)
    file_extension = os.path.splitext(file_name[-1])[-1]
    print(file_extension)
    return file_extension


if __name__ == '__main__':
    id = '5eb87d47ffd86e000604b38a'
    link_apod = 'https://api.nasa.gov/planetary/apod'
    link_epic = 'https://api.nasa.gov/EPIC/api/natural'
    count = 40
    save_picture(link_apod, nasa_api_key, count)
    save_picture(link_epic, nasa_api_key, count)