from django.test import TestCase, Client
from django.conf import settings
import os
from .models import Account, Post, Comment
from datetime import datetime, date


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

#
# class NewsTestCase(TestCase):
#     def setUp(self):
#         self.test_client = Client()
#         self.test_content = 'content'
#
#     def test_get_news(self):
#         response = self.client.post('/news/', data=self.comment_data)
#         self.assertEquals(response.status_code, 201, "successful")
#         self.assertEquals(comment.content, self.test_content)


