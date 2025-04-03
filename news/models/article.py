from django.db import models
from news.models import CustomUser

class Category(models.Model):
    name = models.CharField(max_length=255)
   

class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='images/article/', null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(blank=True, null=True)
    views = models.IntegerField(default=0)