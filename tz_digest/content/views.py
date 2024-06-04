from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from .models import *
from .serializer import *


class ArticleViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Article.objects.select_related("author").all()
        # Eager load the author field
        serializer = ArticleSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, slug=None):
        queryset = Article.objects.select_related("author").all()
        article = get_object_or_404(queryset, slug=slug)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)


 
