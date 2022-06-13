from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='photos/%Y/%m/%d')
