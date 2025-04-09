from news.permissions import *
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from django.utils.timezone import now
from django.shortcuts import get_object_or_404
import news.models as models
import news.serializers as sers

class NewsPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 100


class NewsAPIView(APIView):
    pagination_class = NewsPagination

    @swagger_auto_schema(tags=['news'])
    def get(self, request):
        articles = models.Article.objects.all()
        ser = sers.ArticleSerializer(articles, many=True)
        return Response(ser.data)
        

    @swagger_auto_schema(tags=['news'], request_body=sers.ArticleSerializer)
    def post(self, request):
        self.permission_classes = [IsAuthenticated, IsAdminOrAuthor]
        self.check_permissions(request)

        article = sers.ArticleSerializer(data=request.data)
        if article.is_valid():
            article.save()
            return Response(article.data)
        return Response(article.errors)
    

class NewsDetailAPIView(APIView):
    @swagger_auto_schema(tags=['news'])
    def get(self, request, pk):
        article = get_object_or_404(models.Article, id=pk)
        ser = sers.ArticleSerializer(article)
        article.views += 1
        article.save(update_fields=['views'])
        return Response(ser.data)
    
    @swagger_auto_schema(tags=['news'], request_body=sers.ArticleSerializer)
    def put(self, request, pk):
        self.permission_classes = [IsAuthenticated, IsAdminOrAuthor]
        self.check_permissions(request)

        article = get_object_or_404(models.Article, id=pk)
        updated = sers.ArticleSerializer(data=request.data, instance=article)
        if updated.is_valid():
            updated.save(updated_at=now().date())
            return Response(updated.data)
        return Response(updated.errors)
    
    @swagger_auto_schema(tags=['news'], request_body=sers.ArticleSerializer)
    def delete(self, request, pk):
        self.permission_classes = [IsAuthenticated, IsAdminOrAuthor]
        self.check_permissions(request)
        
        article = get_object_or_404(models.Article, id=pk)
        article.delete()
        return Response({'message':'deleted'})
        