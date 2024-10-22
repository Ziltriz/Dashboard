from django.urls import path
from .views import PostsView, PostCreate, AuthUser

urlpatterns = [
    path('12/', PostsView.as_view(), name='posts_list'),
    path('create/', PostCreate.as_view(), name='posts_create'),
    path('', AuthUser.as_view(), name='auth_user')
]