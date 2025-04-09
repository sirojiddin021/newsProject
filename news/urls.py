from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
import news.views as views

urlpatterns = [
    path('auth/register/', views.register),
    path('auth/login/', TokenObtainPairView.as_view()),
    path('auth/profile/', views.profile),
    
    path('news/', views.NewsAPIView.as_view()),
    path('news/<int:pk>/', views.NewsDetailAPIView.as_view()),

    path('news/<int:pk>/comments/', views.CommentAPIView.as_view()),
    path('comments/<int:pk>/', views.DeleteComment.as_view()),

    path('news/popular/', views.popular),
    path('news/recent/', views.recent),
    path('news/top-5/', views.top_five),
    path('news/most-viewed/', views.most_viewed),

    path('news/<int:pk>/save/', views.save),
    path('news/<int:pk>/unsave/', views.unsave),
    path('user/saved-news/', views.saved_news),

    path('search/', views.search),
]