from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Book

User = get_user_model()


class BookTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username='auth')
        cls.book = Book.objects.create(
            title='title',
            subtitle='subtitle',
            author=cls.user,
            isbn='1234567890123',
        )

    def test_book_content(self):
        self.assertEqual(self.book.title, 'title')
        self.assertEqual(self.book.subtitle, 'subtitle')
        self.assertEqual(self.book.title, 'title')
        self.assertEqual(self.book.isbn, '1234567890123')
        self.assertEqual(self.book.author.username, 'auth')

    def test_book_listview(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'books/book_list.html')
        self.assertContains(response, 'subtitle')
