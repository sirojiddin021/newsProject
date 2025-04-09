from rest_framework.decorators import api_view
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from django.shortcuts import get_object_or_404
import news.models as models
import news.serializers as sers

@swagger_auto_schema(tags=['bookmarks'], method='get')
@api_view(['GET'])
def saved_news(request, pk=None):
    articles = models.Bookmark.objects.filter(marked_by=request.user)
    ser = sers.BookmarkSerializer(articles, many=True)
    return Response(ser.data)

@swagger_auto_schema(tags=['bookmarks'], request_body=sers.BookmarkSerializer, method='post')
@api_view(['POST'])
def save(request, pk):
    article = get_object_or_404(models.Article, id=pk)
    marked = models.Bookmark.objects.filter(article=article, marked_by=request.user)
    if marked.exists():
        return Response({'message':'already marked'})
    bookmark = models.Bookmark.objects.create(
        article=article, 
        marked_by=request.user,
    )
    ser = sers.BookmarkSerializer(bookmark)
    return Response(ser.data)
    

@swagger_auto_schema(tags=['bookmarks'], method='delete')
@api_view(['DELETE'])
def unsave(request, pk):
    bookmark = models.Bookmark.objects.filter(article_id=pk, marked_by=request.user)
    if bookmark.exists():
        bookmark.delete()
        return Response({'message':'delete'})
    return Response({'message':'not found'})