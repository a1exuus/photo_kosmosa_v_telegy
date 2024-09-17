import requests
import json
import os
from dotenv import load_dotenv
import datetime
import io

load_dotenv()


def save_epic_images(api_key, url):
    params = {
        'api_key': api_key
    }
    response = requests.get(url, params=params)
    jsonq = json.loads(response.text)
    response.raise_for_status()
    for index, image_json in enumerate(jsonq):
        path = f'image/nasa_epic_{index}.png'
        link_epic_archive = 'https://api.nasa.gov/EPIC/archive/natural'
        image_id = image_json['image']
        image_date = datetime.datetime.fromisoformat(image_json['date'])
        parsed_image_date = image_date.strftime('%Y/%m/%d')
        url_a = f'{link_epic_archive}/{parsed_image_date}/png/{image_id}.png'
        response = requests.get(url_a, params=params)
        with io.open(path, 'wb') as file:
            file.write(response.content)


if __name__ == '__main__':
    api_key = os.getenv('NASA_API_KEY')
    link_epic = 'https://api.nasa.gov/EPIC/api/natural'

    save_epic_images(api_key, link_epic)