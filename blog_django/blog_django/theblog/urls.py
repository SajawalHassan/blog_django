from django.urls import path
from .views import HomeView, ArticleDetailView, AddPostView, UpdatePostView, DeletePostView

urlpatterns = [
    path('',  HomeView.as_view(), name="home"),
    path('article/<str:pk>',  ArticleDetailView.as_view(), name="article-detail"),
    path('add_post',  AddPostView.as_view(), name="add-post"),
    path('update_post/<str:pk>',  UpdatePostView.as_view(), name="update-post"),
    path('delete_post/<str:pk>',  DeletePostView.as_view(), name="delete-post"),
]
