from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from drf_yasg.utils import swagger_auto_schema
import news.models as models
import news.serializers as sers

class NewsPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 100



@swagger_auto_schema(tags=['statistics'], method='get')
@api_view(['GET'])
def popular(request):
    articles = models.Article.objects.order_by('-views')
    paginator = NewsPagination()
    result_page = paginator.paginate_queryset(articles, request)
    ser = sers.ArticleSerializer(result_page, many=True)
    return paginator.get_paginated_response(ser.data)


@swagger_auto_schema(tags=['statistics'], method='get')
@api_view(['GET'])
def recent(request):
    articles = models.Article.objects.order_by('-created_at')
    paginator = NewsPagination()
    result_page = paginator.paginate_queryset(articles, request)
    ser = sers.ArticleSerializer(result_page, many=True)
    return paginator.get_paginated_response(ser.data)


@swagger_auto_schema(tags=['statistics'], method='get')
@api_view(['GET'])
def most_viewed(request):
    articles = models.Article.objects.order_by('-views')
    paginator = NewsPagination()
    result_page = paginator.paginate_queryset(articles, request)
    ser = sers.ArticleSerializer(result_page, many=True)
    return paginator.get_paginated_response(ser.data)


@swagger_auto_schema(tags=['statistics'], method='get')
@api_view(['GET'])
def top_five(request):
    articles = models.Article.objects.order_by('-created_at')[:5]
    ser = sers.ArticleSerializer(articles, many=True)
    return Response(ser.data)
