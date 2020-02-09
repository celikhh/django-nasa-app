import requests

from .api_endpoints import API_KEY, apod_url, photo_search_url

apod_final_url = apod_url + API_KEY


def get_picture_of_the_day():
    apod_response = requests.get(apod_final_url)
    apod = apod_response.json()
    return apod


def search_media(keyword):
    keyword.replace(' ', '%20')
    search_response = requests.get(photo_search_url.format(keyword))
    response = search_response.json()
    item_list = response.get('collection').get('items')  # USE GET FOR EMPTY
    response_list = []

    if item_list is not None:
        top6_image = item_list[:6]
        for img in top6_image:
            item = {
                'title': img.get('data')[0].get('title'),
                'href': img.get('links')[0].get('href'),
                'description': img.get('data')[0].get('description_508'),
                'date': img.get('data')[0].get('date_created'),
            }
            response_list.append(item)

    return response_list
