# get latest blog posts and news content from a third party API
import os
import requests
from django.http import HttpResponse


def get_news(request):
    headers = {
        'Content-Type': 'application/json'
    }

    payload = {
        'access_key': os.environ.get('NEWS_API_KEY'),
        'categories': 'technology, business',
        'languages': 'en',
        'sort': 'published_desc',
        'limit': 20,
    }

    url = 'http://api.mediastack.com/v1/news'
    data = requests.get(url, headers=headers, params=payload)
    return HttpResponse(data, content_type="application/json")

