from rest_framework.decorators import api_view
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
import news.models as models
import news.serializers as sers

@swagger_auto_schema(tags=['search'], method='get')
@api_view(['GET'])
def search(request):
    query = request.GET.get('query', '')
    if query:
        search = models.Article.objects.filter(content__icontains=query)
        result = sers.ArticleSerializer(search, many=True)
        return Response(result.data)
    return Response({'message':'invalid request'})