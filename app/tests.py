from django.test import TestCase, Client, RequestFactory
from unittest.mock import patch, Mock
from django.conf import settings
from django.urls import reverse
import os
# import json
from .models import Account, Post, Comment
from datetime import datetime, date
from .newsAPI import get_news
from .helper import scramble_uploaded_image, unique_slug_generator


# Create your tests here.
class AccountTestCase(TestCase):
    def setUp(self):
        self.test_client = Client()
        self.test_first_name = 'Tomiwa'
        self.test_last_name = 'Obanla'
        self.test_username = 'tomiwa'
        self.test_email = 'obanlatomiwa@gmail.com'
        self.test_phone_number = '+23400000000'
        self.test_gender = 'm'
        # self.test_date_of_birth = '1960-10-01'
        self.test_date_of_birth = date(1960, 10, 1)

        self.account_data = {
            "first_name": self.test_first_name,
            "last_name": self.test_last_name,
            "username": self.test_username,
            "phone_number": self.test_phone_number,
            "email": self.test_email,
            "gender": self.test_gender,
            "date_of_birth": self.test_date_of_birth
        }

    def test_create_account(self):
        response = self.client.post('/account/', data=self.account_data)
        # print(response.text)
        self.assertEquals(response.status_code, 201, "successful")
        account = Account.objects.get(username=self.test_username)

        self.assertEquals(account.username, self.test_username)
        self.assertEquals(account.first_name, self.test_first_name)
        self.assertEquals(account.last_name, self.test_last_name)
        self.assertEquals(account.email, self.test_email)
        self.assertEquals(account.phone_number, self.test_phone_number)
        self.assertEquals(account.gender, self.test_gender)
        self.assertEquals(account.date_of_birth, self.test_date_of_birth)

    def test_get_account(self):
        response = self.client.get('/account/')
        self.assertEquals(response.status_code, 200, "successful")


class PostTestCase(TestCase):
    def setUp(self):
        self.test_client = Client()
        self.test_title = 'Post'
        self.test_content = 'content'
        self.test_draft = False

        self.dob = date(1960, 10, 1)

        self.test_user = Account.objects.create(first_name='tomiwa', last_name='obanla',
                                                phone_number='+23400000000', username='tomiwa',
                                                email='obanlatomiwa@gmail.com', gender='m',
                                                date_of_birth=self.dob)

        self.post_data = {
            "title": self.test_title,
            "content": self.test_content,
            "draft": self.test_draft,
        }

    def test_create_post(self):
        response = self.client.post('/post/', data=self.post_data)
        self.assertEquals(response.status_code, 201, "successful")
        post = Post.objects.get(user=self.test_user)
        self.assertEquals(post.title, self.test_title)
        self.assertEquals(post.content, self.test_content)
        self.assertEquals(post.draft, self.test_draft)
        self.assertEquals(post.user, self.test_user)

    def test_get_post(self):
        response = self.client.get('/post/')
        self.assertEquals(response.status_code, 200, "successful")


class CommentTestCase(TestCase):
    def setUp(self):
        self.test_client = Client()
        self.test_content = 'content'
        self.dob = date(1960, 10, 1)

        self.test_user = Account.objects.create(first_name='tomiwa', last_name='obanla',
                                                phone_number='+23400000000', username='tomiwa',
                                                email='obanlatomiwa@gmail.com', gender='m',
                                                date_of_birth=self.dob)

        self.test_post = Post.objects.create(title='test', content='test', draft=True, user=self.test_user)
        self.comment_data = {
            "content": self.test_content,
            "post": 1
        }

    def test_create_comment(self):
        response = self.client.post('/comment/', data=self.comment_data)
        self.assertEquals(response.status_code, 201, "successful")
        comment = Comment.objects.get(user=self.test_user)
        self.assertEquals(comment.content, self.test_content)
        self.assertEquals(comment.user, self.test_user)
        self.assertEquals(comment.post, self.test_post)

    def test_get_comment(self):
        response = self.client.get('/comment/')
        self.assertEquals(response.status_code, 200, "successful")


class HelperTestCase(TestCase):
    def setUp(self):
        self.test_image_name = 'blueloop.png'

    def test_image_name_generation(self):
        result = scramble_uploaded_image(self, self.test_image_name)
        self.assertNotEquals(result.split('.')[0], 'blueloop')


class NewsTestCase(TestCase):
    def setUp(self):
        self.status_code = 200
        self.test_json = {
            "pagination": {
                "limit": 20,
                "offset": 0,
                "count": 1,
                "total": 10
            },
            "data": [
                {
                    "author": "zee business",
                    "title": "Gold Price Outlook – Know how US job numbers to impact price movement on Monday – "
                             "Experts give trading, investment strategy",
                    "description": "Gold Price Outlook – Gold traded in a rangebound manner over this week. The MCX "
                                   "Gold Futures traded between Rs 48,500 and Rs 49,500 with an overall dip of 1 per "
                                   "cent during the week. Over the last three months, yellow metal has appreciated by "
                                   "almost 10 per cent. Will the trend continue over the next week too or is there a "
                                   "likelihood of a one-way movement?",
                    "url": "https://www.zeebiz.com/personal-finance-news/news-gold-price-outlook-know-how-us-job"
                           "-numbers-to-impact-price-movement-on-monday-experts-give-trading-investment-strategy"
                           "-158066",
                    "source": "Zee Business",
                    "image": None,
                    "category": "business",
                    "language": "en",
                    "country": "us",
                    "published_at": "2021-06-06T10:37:47+00:00"
                },
            ]
        }

    @patch("requests.get")
    def test_get_news(self, mocked):
        mock_response = Mock()
        result = {
            "pagination": {
                "limit": 20,
                "offset": 0,
                "count": 1,
                "total": 10
            },
            "data": [
                {
                    "author": "zee business",
                    "title": "Gold Price Outlook – Know how US job numbers to impact price movement on Monday – "
                             "Experts give trading, investment strategy",
                    "description": "Gold Price Outlook – Gold traded in a rangebound manner over this week. The MCX "
                                   "Gold Futures traded between Rs 48,500 and Rs 49,500 with an overall dip of 1 per "
                                   "cent during the week. Over the last three months, yellow metal has appreciated by "
                                   "almost 10 per cent. Will the trend continue over the next week too or is there a "
                                   "likelihood of a one-way movement?",
                    "url": "https://www.zeebiz.com/personal-finance-news/news-gold-price-outlook-know-how-us-job"
                           "-numbers-to-impact-price-movement-on-monday-experts-give-trading-investment-strategy"
                           "-158066",
                    "source": "Zee Business",
                    "image": None,
                    "category": "business",
                    "language": "en",
                    "country": "us",
                    "published_at": "2021-06-06T10:37:47+00:00"
                },
            ]
        }

        # Define response data for my Mock object
        mock_response.result = result
        mock_response.status_code = 200

        # Define response for the fake API
        mocked.return_value = mock_response

        # Call the function
        self.assertEquals(get_news(mock_response).status_code, 200, "success")
        self.assertEquals(get_news(mock_response).headers['Content-Type'], 'application/json')
