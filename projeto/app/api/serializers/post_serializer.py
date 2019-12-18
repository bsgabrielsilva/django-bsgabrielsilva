from django.contrib.auth.models import User
from rest_framework import serializers
from ...models import Post, Category


class CategoryNestedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = ('created_at', 'updated_at')


class UserNestedSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', )


class PostSerializer(serializers.ModelSerializer):
    categories = CategoryNestedSerializer(many=True)
    user = UserNestedSerializer(many=False)

    class Meta:
        model = Post
        fields = '__all__'
        depth = 1
