import requests
import json
import argparse
import os

os.makedirs('image', exist_ok=True)


def fetch_spacex_last_launch(url, params, launch_id):
    if launch_id != None:
        url = 'https://api.spacexdata.com/v5/launches/'
        params = {'id': launch_id}
    response = requests.get(url, params=params)
    response.raise_for_status()
    datas = json.loads(response.text)
    for index, data in enumerate(datas):
        path = f'image/space_x_{index}.jpeg'
        if data['links']['flickr']['original']:
            images_links = data['links']['flickr']['original']
            for image_link in images_links:
                response = requests.get(image_link)
                with open(path, 'wb') as file:
                    file.write(response.content)


if __name__ == '__main__':
    past_spacex_url = 'https://api.spacexdata.com/v5/launches/past'
    parser = argparse.ArgumentParser(
        description='Данный скрипт получает на вход id любого запуска компании SpaceX и сохраняет фотографии с данного запуска в папку images(если такова отсутствует, он создает её в директории, в которой находиться сам). Если id не был указан, скачивает фотографии с прошлого запуска SpaceX.'
    )
    parser.add_argument('--id',
                        help='ID запуска SpaceX',
                        type=str)
    args = parser.parse_args()
    params = {}
    fetch_spacex_last_launch(past_spacex_url, params, args.id)