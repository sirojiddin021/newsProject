from rest_framework import serializers
from news.serializers import ArticleSerializer, UserSerializer
import news.models as models


class BookmarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Bookmark
        fields = '__all__'

    def to_representation(self, instance):
        bookmark = super().to_representation(instance)
        bookmark['article'] = ArticleSerializer(instance.article).data
        bookmark['marked_by'] = UserSerializer(instance.marked_by).data
        return bookmark