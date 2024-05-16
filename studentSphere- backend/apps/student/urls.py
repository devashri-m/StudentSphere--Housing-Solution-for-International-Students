from django.conf.urls import url
from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from apps.student.views import StudentCRUD, StudentLogin, StudentLogout

urlpatterns = [
    url(r'^user/$', StudentCRUD.as_view(), name="student-list-create"),
    url(r'^user/(?P<userid>[A-Za-z0-9]+)/$', StudentCRUD.as_view(), name="student-detail"),
    url(r'^login/$', StudentLogin.as_view(), name="student-login"),
    url(r'^logout/$', StudentLogout.as_view(), name="student-logout"),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
