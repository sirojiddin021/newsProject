from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from django.shortcuts import get_object_or_404
import news.models as models
import news.serializers as sers


class CommentAPIView(APIView):
    @swagger_auto_schema(tags=['comments'])
    def get(self, request, pk):
        comments = models.Comment.objects.filter(news_id=pk)
        if comments.exists():
            ser = sers.CommentSerializer(comments, many=True)
            return Response(ser.data)
        return Response({'message':'not comments yet'})
    
    @swagger_auto_schema(tags=['comments'], request_body=sers.CommentSerializer)
    def post(self, request, pk):
        self.permission_classes = [IsAuthenticated]
        self.check_permissions(request)

        comment = sers.CommentSerializer(data=request.data)
        if comment.is_valid():
            comment.save(news_id=pk, author=request.user)
            return Response(comment.data)
        return Response(comment.errors)
    
    
class DeleteComment(APIView):
    @swagger_auto_schema(tags=['comments'])
    def delete(self, request, pk):
        comment = models.Comment.objects.get(id=pk)
        if comment.author == request.user or request.user.role == 'admin':
            comment.delete()
            return Response({'message':'deleted'})
        return Response({'message':'not allowed'})
