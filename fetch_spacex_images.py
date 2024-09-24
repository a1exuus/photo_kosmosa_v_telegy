import requests
import argparse
import os
import save_picture


def fetch_spacex_last_launch(launch_id):
    url = 'https://api.spacexdata.com/v5/launches/'
    params = {'id': launch_id}
    response = requests.get(url, params=params)
    response.raise_for_status()
    pictures = response.json()
    for index, picture in enumerate(pictures):
        path = f'image/space_x_{index}.jpeg'
        if picture['links']['flickr']['original']:
            images_links = picture['links']['flickr']['original']
            params = {}
            for image_link in images_links:
                save_picture.save_picture(image_link, path, params)


if __name__ == '__main__':
    os.makedirs('image', exist_ok=True)
    parser = argparse.ArgumentParser(
        description='Данный скрипт получает на вход id любого запуска компании SpaceX и сохраняет фотографии с данного запуска в папку images(если такова отсутствует, он создает её в директории, в которой находиться сам). Если id не был указан, скачивает фотографии с прошлого запуска SpaceX.'
    )
    parser.add_argument('--id',
                        help='ID запуска SpaceX',
                        type=str,
                        default='past'
                        )
    args = parser.parse_args()
    fetch_spacex_last_launch(args.id)