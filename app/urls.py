from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view
from .views import AccountViewSet, PostViewSet, CommentViewSet
from .newsAPI import get_news

schema_view = get_schema_view(title='Blog API')
router = DefaultRouter()
router.register(r'account', AccountViewSet)
router.register(r'post', PostViewSet)
router.register(r'comment', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('news/', get_news, name='news'),

]
