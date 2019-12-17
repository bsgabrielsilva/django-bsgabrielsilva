from django.contrib import admin
from .models import Category, Post
from .models_admin import *

# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
