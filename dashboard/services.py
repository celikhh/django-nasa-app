import requests

# h.huseyin33@gmail.com
from django.shortcuts import render

API_KEY = 'sesZBXLz2b6ccaECcoeUDMWbuPmOd2BekTOGfkdZ'  # PUT INTO SETTINGS
url = 'https://api.nasa.gov/planetary/apod?api_key=sesZBXLz2b6ccaECcoeUDMWbuPmOd2BekTOGfkdZ'


def get_picture_of_the_day():
    apod_response = requests.get('https://api.nasa.gov/planetary/apod?api_key=sesZBXLz2b6ccaECcoeUDMWbuPmOd2BekTOGfkdZ')
    apod = apod_response.json()
    return apod


def search_media(keyword):
    keyword.replace(' ', '%20')
    search_response = requests.get('https://images-api.nasa.gov/search?q={}'.format(keyword))
    response = search_response.json()
    item_list = response['items']
    top6 = item_list[:5]
    return top6
