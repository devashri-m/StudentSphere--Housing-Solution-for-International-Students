# favorites/urls.py

from django.urls import path
from .views import FavoriteApartments

urlpatterns = [
    path('favorites/', FavoriteApartments.as_view(), name='favorite-apartments'),
]
