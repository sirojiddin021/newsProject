from django.db import models
from news.models import Article, CustomUser


class Bookmark(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    marked_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)