from rest_framework import serializers
from news.serializers import UserSerializer, ArticleSerializer
import news.models as models


class CommentSerializer(serializers.ModelSerializer):
    news = ArticleSerializer(read_only=True)
    author = UserSerializer(read_only=True)
    news_id = serializers.PrimaryKeyRelatedField(queryset=models.Article.objects.all(), source='news', write_only=True)
    author_id = serializers.PrimaryKeyRelatedField(queryset=models.CustomUser.objects.all(), source='author', write_only=True)
    class Meta:
        model = models.Comment
        fields = '__all__'