from django.db import models
from django.contrib.postgres.fields import ArrayField


class News(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    tags = models.CharField(max_length=500)
    source = models.CharField(max_length=100)
