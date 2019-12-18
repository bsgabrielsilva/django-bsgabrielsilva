from rest_framework import viewsets
from ..serializers import CategorySerializer
from ...models import Category


class CategoryViewset(viewsets.ModelViewSet):
    http_method_names = ['get', ]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()