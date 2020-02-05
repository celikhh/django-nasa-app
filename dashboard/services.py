import requests

# h.huseyin33@gmail.com
from django.shortcuts import render

API_KEY = 'sesZBXLz2b6ccaECcoeUDMWbuPmOd2BekTOGfkdZ'  # PUT INTO SETTINGS
url = 'https://api.nasa.gov/planetary/apod?api_key=sesZBXLz2b6ccaECcoeUDMWbuPmOd2BekTOGfkdZ'  # PUT INTO SETTINGS


def get_picture_of_the_day():
    apod_response = requests.get('https://api.nasa.gov/planetary/apod?api_key=sesZBXLz2b6ccaECcoeUDMWbuPmOd2BekTOGfkdZ')
    apod = apod_response.json()
    return apod


def search_media(keyword):
    keyword.replace(' ', '%20')
    search_response = requests.get('https://images-api.nasa.gov/search?q={}&media_type=image'.format(keyword))
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
