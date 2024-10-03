import requests
import os
from dotenv import load_dotenv
import save_picture


def save_apod_pictures(url, api_key, count):
    params = {
        'api_key': api_key,
        'count': count
     }
    response = requests.get(url, params=params)
    response.raise_for_status()
    pictures = response.json()
    params={}
    for index, picture in enumerate(pictures):
        path = f'image/nasa_apod_{index}.png'
        image_url = picture['url']
        save_picture.save_picture(image_url, path, params)

if __name__ == '__main__':
    load_dotenv()
    os.makedirs('image', exist_ok=True)
    api_key = os.getenv('NASA_API_KEY')
    link_apod = 'https://api.nasa.gov/planetary/apod'
    count = 40
    save_apod_pictures(link_apod, api_key, count)