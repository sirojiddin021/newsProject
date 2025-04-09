from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from news.serializers import UserSerializer
from drf_yasg.utils import swagger_auto_schema

@swagger_auto_schema(tags=['auth'], method='get')
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def profile(request):
    user = UserSerializer(request.user)
    return Response(user.data)


@swagger_auto_schema(method='post', tags=['auth'], request_body=UserSerializer)
@api_view(['POST'])
def register(request):
    user = UserSerializer(data=request.data)
    if user.is_valid():
        user.save()
        return Response(user.data)
    return Response({'message':'could not create user'})