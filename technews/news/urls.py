from .views import NewsView, NewsDetailView, CreateNewsView, UpdateNewsView, DeleteNewsView, GetNewsByTagsView
from django.urls import path

urlpatterns = [
    path('news/', NewsView.as_view()),
    path('news/<int:pk>', NewsDetailView.as_view()),
    path('news/create', CreateNewsView.as_view()),
    path('news/update/<int:pk>', UpdateNewsView.as_view()),
    path('news/delete/<int:pk>', DeleteNewsView.as_view()),
    path('news/filter/', GetNewsByTagsView.as_view()),
]
