from django.db import models


class Book(models.Model):
    googleapis_id = models.CharField(max_length=32, unique=True)
    title = models.CharField(max_length=255, null=True)
    authors = models.CharField(max_length=255, null=True)
    published_date = models.CharField(max_length=15, null=True)
    categories = models.CharField(max_length=255, null=True)
    thumbnail = models.URLField(null=True)
