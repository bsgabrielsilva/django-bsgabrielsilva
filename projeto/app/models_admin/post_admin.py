from django.contrib import admin
from ..forms import PostForm


class PostAdmin(admin.ModelAdmin):
    form = PostForm
