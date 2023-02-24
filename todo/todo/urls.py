from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from authors.views import AuthorModelViewSet
from rest_framework import permissions, routers
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from mainapp import views
from rest_framework.generics import DestroyAPIView, UpdateAPIView
from rest_framework.authtoken import views
from mainapp.views import UserViewSet, NotesViewSet


router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('notes', NotesViewSet)

filter_router = DefaultRouter()
filter_router.register('param', views.ArticleParamFilterViewSet)

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('', include('to_do.urls')),
    path('views/api-view/', views.ArticleAPIVIew.as_view()),
    path('generic/retrieve/<int:pk>/', views.ArticleRetrieveAPIView.as_view()),
    path('viewsets/', include(router.urls)),
    path('filters/kwargs/<str:name>/', views.ArticleKwargsFilterView.as_view()),
    path('filters/', include(filter_router.urls)),
]

