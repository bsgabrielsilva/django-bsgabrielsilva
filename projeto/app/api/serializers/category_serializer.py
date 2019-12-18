from rest_framework import serializers
from ...models import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('slug', 'name', 'created_at', 'updated_at', 'posts')
        depth = 1