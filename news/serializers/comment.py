from rest_framework import serializers
from news.serializers import UserSerializer, ArticleSerializer
import news.models as models


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Comment
        fields = '__all__'
    
    def to_representation(self, instance):
        comment = super().to_representation(instance)
        comment['author'] = UserSerializer(instance.author).data
        comment['news'] = ArticleSerializer(instance.news).data
        return comment