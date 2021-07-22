from django.urls import path, include
from rest_framework import urlpatterns
from tweets.api import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'tweets',views.TweetViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('add-tweet/', views.TweetCreateAPIView.as_view(), name='add-tweet'),
    path('tweet/', views.TweetCreateAPIView.as_view(), name='tweet')
]