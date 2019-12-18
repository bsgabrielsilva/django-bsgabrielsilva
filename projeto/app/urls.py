from django.urls import path
from .views import *


urlpatterns = [
    path('', home_blog, name='home_blog'),
    path('categories/', categories_blog, name='categories_blog'),
    path('categories/<slug:pk>', category_detail, name='category_detail'),
    path('post/<slug:pk>', post_detail, name='post_detail')
]