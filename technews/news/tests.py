from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import News


class NewsTests(APITestCase):

    def setUp(self):
        self.news1 = News.objects.create(
            title="News 1",
            body="Body of news 1",
            tags="tag1,tag2",
            source="Source 1"
        )
        self.news2 = News.objects.create(
            title="News 2",
            body="Body of news 2",
            tags="tag2,tag3",
            source="Source 2"
        )

    def test_list_news(self):
        response = self.client.get(reverse('news-list'))
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_news(self):
        response = self.client.get(
            reverse('news-detail', kwargs={'pk': self.news1.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.news1.title)

    def test_create_news(self):
        data = {
            'title': 'News 3',
            'body': 'Body of news 3',
            'tags': 'tag3,tag4',
            'source': 'Source 3'
        }
        response = self.client.post(
            reverse('news-create'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(News.objects.count(), 3)

    def test_update_news(self):
        data = {
            'title': 'Updated News 1',
            'body': 'Updated body of news 1',
            'tags': 'tag1,tag3',
            'source': 'Updated Source 1'
        }
        response = self.client.put(
            reverse('news-update', kwargs={'pk': self.news1.pk}), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.news1.refresh_from_db()
        self.assertEqual(self.news1.title, 'Updated News 1')

    def test_delete_news(self):
        response = self.client.delete(
            reverse('news-delete', kwargs={'pk': self.news1.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(News.objects.count(), 1)
