from django.db import models
from news.models import Article, CustomUser


class Comment(models.Model):
    news = models.ForeignKey(Article, on_delete=models.CASCADE)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateField(auto_now_add=True)