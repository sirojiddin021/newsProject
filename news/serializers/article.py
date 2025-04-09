from rest_framework import serializers
from news.serializers import UserSerializer
import news.models as models


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = '__all__'


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Article
        fields = '__all__'

    def to_representation(self, instance):
        article = super().to_representation(instance)
        article['category'] = CategorySerializer(instance.category).data
        article['author'] = UserSerializer(instance.author).data
        return article