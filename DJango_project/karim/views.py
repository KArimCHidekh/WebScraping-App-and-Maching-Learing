from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
#-----------------
from rest_framework.parsers import JSONParser


def index(request):
    return HttpResponse("Hello, Mila . You're at the Karim index.")
#---------------
from rest_framework import viewsets

from .serializers import  ArticleSerializer
from .models import Article
from rest_framework.views import APIView


#class ArticleViewSet(viewsets.ModelViewSet):
class ArticleViewSet(APIView):

    serializer_class = ArticleSerializer

    parser_classes = [JSONParser]
    """
    def get_queryset(self):
        search_tag = self.kwargs['tag']
        queryset = Article.objects.all()
        queryset = queryset.filter(tag=search_tag )
        return queryset
"""

    def post(self, request, format=None):
        queryset = Article.objects.all().order_by('id')
        file_tag = request.data['tag']



        if file_tag !='all':
            queryset = queryset.filter(tag__contains=file_tag)
            serializer = ArticleSerializer(queryset, many=True)
            return Response( serializer.data)
        else:
            serializer = ArticleSerializer(queryset, many=True)
            return Response(serializer.data)
        #return Response({'received data': request.data})


#-----------------
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated  # <-- Here
class HelloView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)