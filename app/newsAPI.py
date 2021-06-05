# get latest blog posts and news content from a third party API
import os
import requests
from django.http import HttpResponse


def get_news():
        print(os.environ.get('NEWS_API_KEY'))
        payload = {
            # 'access_key': os.environ.get('NEWS_API_KEY'),
            'access_key': '2e9d22cbbef62a5227ba5b690635702f',
            'categories': 'technology, business',
            'languages': 'en',
            'sort': 'published_desc',
            'limit': 20,
        }

        url = 'https://api.mediastack.com/v1/news'

        data = requests.get(url, params=payload)
        print(data.url)
        return HttpResponse(data.json())



