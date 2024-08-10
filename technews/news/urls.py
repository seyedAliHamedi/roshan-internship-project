from .views import NewsView, NewsDetailView, CreateNewsView, UpdateNewsView, DeleteNewsView, GetNewsByTagsView
from django.urls import path

urlpatterns = [
    path('news/', NewsView.as_view(), name='news-list'),
    path('news/<int:pk>/', NewsDetailView.as_view(), name='news-detail'),
    path('news/create/', CreateNewsView.as_view(), name='news-create'),
    path('news/update/<int:pk>/', UpdateNewsView.as_view(), name='news-update'),
    path('news/delete/<int:pk>/', DeleteNewsView.as_view(), name='news-delete'),
    path('news/filter/', GetNewsByTagsView.as_view(), name='news-filter'),
]
