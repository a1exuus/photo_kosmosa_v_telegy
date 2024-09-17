import json
import requests
import os
from dotenv import load_dotenv

load_dotenv()
os.makedirs('image', exist_ok=True)


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


if __name__ == '__main__':
    api_key = os.getenv('NASA_API_KEY')
    link_apod = 'https://api.nasa.gov/planetary/apod'
    count = 40
    save_apod_picture(link_apod, api_key, count)