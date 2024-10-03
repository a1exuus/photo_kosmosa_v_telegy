import requests
import os
from dotenv import load_dotenv
import datetime
import save_picture


def save_epic_images(api_key, url):
    params = {
        'api_key': api_key
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    pictures = response.json()
    for index, picture in enumerate(pictures):
        path = f'image/nasa_epic_{index}.png'
        link_epic_archive = 'https://api.nasa.gov/EPIC/archive/natural'
        image_id = picture['image']
        image_date = datetime.datetime.fromisoformat(picture['date'])
        parsed_image_date = image_date.strftime('%Y/%m/%d')
        parsed_url = f'{link_epic_archive}/{parsed_image_date}/png/{image_id}.png'
        save_picture.save_picture(parsed_url, path, params)


if __name__ == '__main__':
    load_dotenv()
    api_key = os.getenv('NASA_API_KEY')
    epic_link = 'https://api.nasa.gov/EPIC/api/natural'

    save_epic_images(api_key, epic_link)