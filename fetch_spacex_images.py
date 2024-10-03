import requests
import argparse
import os
import save_picture


def fetch_spacex_launch(launch_id):
    url = 'https://api.spacexdata.com/v5/launches/'
    params = {'id': launch_id}
    if 'latest' in launch_id:
        params = {}
    response = requests.get(url, params=params)
    response.raise_for_status()
    pictures = response.json()
    for picture in reversed(pictures):
        if picture['links']['flickr']['original']:
            images_links = picture['links']['flickr']['original']
            for index, image_link in enumerate(images_links):
                print(images_links)
                path = f'image/space_x_{index}.jpeg'
                save_picture.save_picture(image_link, path, params)
            break     


if __name__ == '__main__':
    os.makedirs('image', exist_ok=True)
    parser = argparse.ArgumentParser(
        description='Данный скрипт получает на вход id любого запуска компании SpaceX и сохраняет фотографии с данного запуска в папку images(если такова отсутствует, он создает её в директории, в которой находиться сам). Если id не был указан, скачивает фотографии с прошлого запуска SpaceX.'
    )
    parser.add_argument('--id',
                        help='ID запуска SpaceX',
                        type=str,
                        default='latest'
                        )
    args = parser.parse_args()
    fetch_spacex_launch(args.id)