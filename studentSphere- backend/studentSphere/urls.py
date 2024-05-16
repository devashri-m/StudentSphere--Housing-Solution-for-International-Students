"""
URL configuration for studentSphere project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
#from django.urls import path
# from student.views import StudentListCreateView, StudentDetailView



# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('students/', StudentListCreateView.as_view(), name='student-list-create'),
#     path('students/<int:pk>/', StudentDetailView.as_view(), name='student-detail'),
# ]

# from django.conf.urls import url
# #from apps.student.views import *
# from student.views import StudentCRUD


# urlpatterns = [
#      url(r'^user/$', StudentCRUD.as_view(), name= "Student CRUD"),
#      url(r'^user/(?P<userid>[A-Za-z0-9]+)/$', StudentCRUD.as_view(), name="Student CRUD"),
# ]

from django.urls import include, path  # Import 'path'
from .utils import TokenExpiryCheck

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    path('api/v1/', include('apps.student.urls')),  # Use 'path' instead of 'url'
    path('api/v1/', include('apps.apartments.urls')),
    path('api/v1/', include('apps.favorites.urls')),  # Include the favorites URLs
    path('api/v1/', include('apps.comments.urls')),  # Include the comments URLs

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/token/check-expiry/', TokenExpiryCheck.as_view(), name='token_expiry_check'),

]