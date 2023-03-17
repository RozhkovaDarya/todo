from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes, action
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView
from rest_framework import mixins, viewsets, permissions, generics
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import BasePermission
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from .models import Article, User, Notes
from .serializers import ArticleSerializer, UserSerializer, NotesSerializer, NotesSerializerBase, UserSerializerWithFullName
from .filters import ArticleFilter


class StaffOnly(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_staff


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


class ArticleQuerysetFilterViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = Article.objects.all()
    
    def get_queryset(self):
        return Article.objects.filter(name__contains='python')


class ArticleKwargsFilterView(ListAPIView):
    serializer_class = ArticleSerializer
    
    def get_queryset(self):
        name = self.kwargs['name']
        return Article.objects.filter(name__contains=name)


class ArticleParamFilterViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    
    def get_queryset(self):
        name = self.request.query_params.get('name', '')
        articles = Article.objects.all()
        if name:
            articles = articles.filter(name__contains=name)
        return articles


class ArticleDjangoFilterViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    filterset_fields = ['name', 'user']


class ArticleCustomDjangoFilterViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    filterset_class = ArticleFilter


class ArticleLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 2

    
class ArticleLimitOffsetPaginatonViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    pagination_class = ArticleLimitOffsetPagination


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    
class NotesViewSet(viewsets.ModelViewSet):
    # permission_classes = [permissions.IsAuthenticated]
    serializer_class = NotesSerializer
    queryset = Notes.objects.all()

    def get_serializer_class(self):
        if self.request.method in ['GET']:
            return NotesSerializer
        return NotesSerializerBase


class UserListAPIView(viewsets.UserListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer