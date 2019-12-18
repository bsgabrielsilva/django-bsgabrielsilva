from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination

from ..serializers import PostSerializer
from ...models import Post


class PostViewset(viewsets.ModelViewSet):
    http_method_names = ['get', ]
    serializer_class = PostSerializer

    # O endpoint listará apenas os posts que estivem com o publish = True
    queryset = Post.objects.filter(publish=True)
