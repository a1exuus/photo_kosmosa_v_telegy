import io
import requests

def save_picture(url, path, params):
    response = requests.get(url, params=params)
    with io.open(path, 'wb') as file:
        file.write(response.content)