import telegram
from dotenv import load_dotenv
import os
import random
import argparse
import time

load_dotenv()


def get_images_links():
    images_paths = []
    for address, dirs, files in os.walk('photo_kosmosa_v_telegy/image'):
        for name in files:
            image_path = os.path.join(address, name)
            images_paths.append(image_path)
    return images_paths


def send_pictures(chat_id, time_range, images_paths):
    if time_range == None:
        time_range = 14400
    while True:
        random.shuffle(images_paths)
        print(images_paths)
        for image in images_paths:
            print(image)
            bot.send_document(chat_id=chat_id, document=open(image, 'rb'))
            time.sleep(time_range)


if __name__ == '__main__':
    chat_id = os.getenv('TG_CHANNEL_CHAT_ID')
    bot_token = os.getenv('TG_BOT_TOKEN')
    bot = telegram.Bot(token=bot_token)
    parser = argparse.ArgumentParser(
        description='Данный скрипт получает на вход временной диапазон через который вы хотите получать картинки космосав телеграм канал(ссылка тг канала: https://t.me/ptboot)'
    )
    parser.add_argument('--time_range',
                        help='Временной диапазон отправки фотографий(передавайте числа только в секундах, без текста. В 1 часе - 3600 секунд)',
                        type=int
                        )
    args = parser.parse_args()
    send_pictures(chat_id, args.time_range, get_images_links())