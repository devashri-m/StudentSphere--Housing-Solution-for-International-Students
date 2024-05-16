# urls.py

from django.urls import path
from .views import (
    GetCommentsAPIView,
    AddCommentAPIView,
    DeleteCommentAPIView,
    EditCommentAPIView
)

urlpatterns = [
    path('comments/<int:apartment_id>/', GetCommentsAPIView.as_view(), name='get-comments'),
    path('comments/<int:apartment_id>/add/', AddCommentAPIView.as_view(), name='add-comment'),
    path('comments/<int:comment_id>/delete/', DeleteCommentAPIView.as_view(), name='delete-comment'),
    path('comments/<int:comment_id>/edit/', EditCommentAPIView.as_view(), name='edit-comment'),

]
