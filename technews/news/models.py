from django.db import models
from django.contrib.postgres.fields import ArrayField


class News(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    tags = ArrayField(models.CharField(max_length=100),
                      blank=True, default=list)
    source = models.CharField(max_length=100)
