from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Book(models.Model):
    title = models.CharField(max_length=250)
    subtitle = models.CharField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    isbn = models.CharField(max_length=13)

    def __str__(self):
        return self.title
