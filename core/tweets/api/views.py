from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import Tweet
from .serializers import  TweetSerializer #FileSerializer
from rest_framework import generics
from rest_framework.parsers import JSONParser, MultiPartParser

from django.core.files.base import ContentFile
import base64
from django.contrib.auth.models import User
from rest_framework.parsers import FileUploadParser, JSONParser

class TweetViewSet(ReadOnlyModelViewSet):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer

# class TweetCreateAPIView(generics.CreateAPIView):
#     queryset = Tweet.objects.all()
#     serializer_class = TweetSerializer

# class TweetCreateAPIView(APIView):

#     def post(self, request):
#         print(request.data)
#         serializer = TweetSerializer(data=request.data,files=request.FILES)
#         if serializer.is_valid():
#             serializer.save(user=request.user)
#             return Response(
#                 serializer.data,status=status.HTTP_201_CREATED
#             )
#         print(serializer.errors)

class TweetCreateAPIView(generics.CreateAPIView):
    queryset = Tweet.objects.all().order_by('-id')
    serializer_class = TweetSerializer
    parser_classes = [MultiPartParser]

    def perform_create(self, serialzier):
        print(self.request.FILES)
        print(self.request.data)
        serialzier.save(user=User.objects.first())
