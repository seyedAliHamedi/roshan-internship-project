from rest_framework import generics
from .models import News
from .serializer import NewsSerializer
from django.shortcuts import render
import logging

logger = logging.getLogger(__name__)


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
        logger.debug(f'Received tags query parameter: {tags}')
        if tags:
            tags_list = [tag.strip() for tag in tags.split(',')]
            queryset = queryset.filter(tags__name__in=tags_list).distinct()
            logger.debug(f'Filtered queryset: {queryset.query}')
        return queryset
