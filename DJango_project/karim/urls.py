from django.urls import path

from . import views
from django.urls import include, path
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
#router.register(r'articles', views.ArticleViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', views.index, name='index'),
    path('', include(router.urls)),
    #path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('hello/', views.HelloView.as_view(), name='hello'),
    path('articles/', views.ArticleViewSet.as_view()),
]
