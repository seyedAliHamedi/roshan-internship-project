from rest_framework import generics
from .models import News
from .serializer import NewsSerializer

"""
views.py

    This module contains the views for the Tech News backend project. It includes 
    views to list news articles, retrieve a specific article, create new articles, 
    update existing articles, delete articles, and filter articles by tags.

Classes:
    NewsView: Lists all news articles.
    NewsDetailView: Retrieves a specific news article by ID.
    CreateNewsView: Creates a new news article.
    UpdateNewsView: Updates an existing news article by ID.
    DeleteNewsView: Deletes a news article by ID.
    GetNewsByTagsView: Filters news articles by tags.

API Endpoints:
    - GET /api/news/ : List all news articles (NewsView).
    - GET /api/news/<id>/ : Retrieve a specific news article by ID (NewsDetailView).
    - POST /api/news/ : Create a new news article (CreateNewsView).
    - PUT /api/news/<id>/ : Update an existing news article by ID (UpdateNewsView).
    - DELETE /api/news/<id>/ : Delete a news article by ID (DeleteNewsView).
    - GET /api/news/filter-by-tags/?tags=<tags> : Filter news articles by tags (GetNewsByTagsView).
"""



class NewsView(generics.ListAPIView):
    serializer_class = NewsSerializer
    queryset = News.objects.all()


class NewsDetailView(generics.RetrieveAPIView):
    serializer_class = NewsSerializer
    queryset = News.objects.all()


class CreateNewsView(generics.CreateAPIView):
    serializer_class = NewsSerializer
    queryset = News.objects.all()


class UpdateNewsView(generics.UpdateAPIView):
    serializer_class = NewsSerializer
    queryset = News.objects.all()


class DeleteNewsView(generics.DestroyAPIView):
    serializer_class = NewsSerializer
    queryset = News.objects.all()


class GetNewsByTagsView(generics.ListAPIView):
    serializer_class = NewsSerializer
    queryset = News.objects.all()

    def get_queryset(self):
        queryset = News.objects.all()
        tags = self.request.query_params.get('tags', None)
        if tags:
            tags_list = [tag.strip() for tag in tags.split(',')]
            queryset = queryset.filter(tags__name__in=tags_list).distinct()
        return queryset
