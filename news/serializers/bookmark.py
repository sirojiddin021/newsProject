from rest_framework import serializers
from news.serializers import ArticleSerializer, UserSerializer
import news.models as models


class BookmarkSerializer(serializers.ModelSerializer):
    article = ArticleSerializer()
    marked_by = UserSerializer()
    class Meta:
        model = models.Bookmark
        fields = '__all__'