from django.urls import include, path

from .views import BookApiListView

urlpatterns = [
    path('', BookApiListView.as_view(), name='book_list'),
]