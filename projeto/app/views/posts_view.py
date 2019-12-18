import json

from django.core.paginator import InvalidPage, Paginator
from django.shortcuts import render, get_object_or_404
from ..models import Post

ITEM_PER_PAGE = 10


def home_blog(request, template_name="blog/posts.html"):
    page = request.GET.get('page')
    busca = request.GET.get('busca')
    if busca is None:
        paginator = Paginator(Post.objects.all(), ITEM_PER_PAGE)
    else:
        paginator = Paginator(Post.objects.filter(title__icontains=busca), ITEM_PER_PAGE)
    try:
        posts = paginator.page(page)
    except InvalidPage:
        posts = paginator.page(1)
    return render(request, template_name, {'posts': posts})


def post_detail(request, pk, template_name="blog/post_detail.html"):
    post = get_object_or_404(Post, pk=pk)
    return render(request, template_name, {'post': post})