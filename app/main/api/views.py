from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ArticleSerializer, ServiceSerializer
from rest_framework import generics
from app.main.models import Article, Service


class ArticleView(generics.ListAPIView):
    serializer_class = ArticleSerializer

    def get_queryset(self):

        return Article.objects.filter(active=True, belong_to__name='pwud')


class ServiceView(generics.ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
