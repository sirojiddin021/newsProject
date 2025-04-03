from rest_framework import serializers
from news.serializers import UserSerializer
import news.models as models


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = '__all__'


class ArticleSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    author = UserSerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(queryset=models.Category.objects.all(), source='category', write_only=True)
    author_id = serializers.PrimaryKeyRelatedField(queryset=models.CustomUser.objects.all(), source='author', write_only=True)
    class Meta:
        model = models.Article
        fields = '__all__'