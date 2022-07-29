from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from books.models import Book

User = get_user_model()


class APITests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username='auth')
        cls.book = Book.objects.create(
            title='title',
            subtitle='subtitle',
            author=cls.user,
            isbn='1234567890123'
        )

    def test_api_listview(self):
        response = self.client.get(reverse('book_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.book)
        self.assertEqual(Book.objects.count(), 1)
