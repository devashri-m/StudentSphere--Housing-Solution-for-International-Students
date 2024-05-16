
from django.urls import path
from . import views

from .views import ApartmentList, ApartmentDetail  # Make sure this line is present

urlpatterns = [
    path('apartments/', ApartmentList.as_view(), name='apartment-list'),
    path('apartments/<int:pk>/', ApartmentDetail.as_view(), name='apartment-detail'),

]
