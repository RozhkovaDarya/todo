from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from .models import Article
from rest_framework.response import Response
from .serializers import ArticleSerializer
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from rest_framework import mixins


class ArticleAPIVIew(APIView):
    renderer_classes = [JSONRenderer]
    
    def get(self, request, format=None):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)
    

class ArticleListAPIView(ListAPIView):
    renderer_classes = [JSONRenderer]
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    
class ArticleCreateAPIView(CreateAPIView):
    renderer_classes = [JSONRenderer]
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    
    
class ArticleRetrieveAPIView(RetrieveAPIView):
    renderer_classes = [JSONRenderer]
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
     
    
@api_view(['GET'])
@renderer_classes([JSONRenderer])
def article_view(request):
    articles = Article.objects.all()
    serializer = ArticleSerializer(articles, many=True)
    return Response(serializer.data)


class ArticleDestroyAPIView(DestroyAPIView):
   renderer_classes = [JSONRenderer]
   queryset = Article.objects.all()
   serializer_class = ArticleSerializer


class ArticleUpdateAPIView(UpdateAPIView):
   renderer_classes = [JSONRenderer]
   queryset = Article.objects.all()
   serializer_class = ArticleSerializer

class ArticleViewSet(viewsets.ViewSet):
    renderer_classes = [JSONRenderer]
    
    def list(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        article = get_object_or_404(Article, pk=pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)


class ArticleViewSet(viewsets.ViewSet):
    renderer_classes = [JSONRenderer]
    
    @action(detail=True, methods=['get'])
    def article_text_only(self, request, pk=None):
        article = get_object_or_404(Article, pk=pk)
        return Response({'article.text': article.text})
    
    def list(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        article = get_object_or_404(Article, pk=pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)


class ArticleModelViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    renderer_classes = [JSONRenderer]
    serializer_class = ArticleSerializer


class ArticleCustomViewSet(mixins.CreateModelMixin, mixins.ListModelMixin,
                          mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
