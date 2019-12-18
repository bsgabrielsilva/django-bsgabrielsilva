from rest_framework import routers

from django.urls import path, include
from .viewsets import *


router = routers.DefaultRouter()
router.register(r'categories', CategoryViewset, basename="categories")
router.register(r'posts', PostViewset, basename="posts")

urlpatterns = [
    path('', include(router.urls)),
]