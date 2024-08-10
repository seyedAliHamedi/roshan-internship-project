from rest_framework import generics
from .models import News
from .serializer import NewsSerializer
from django.shortcuts import render


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

    def get_queryset(self):
        queryset = super().get_queryset()
        tags = self.request.query_params.get('tags', None)
        if tags:
            tags_list = tags.split(',')
            queryset = queryset.filter(tags__overlap=tags_list)
        return queryset
