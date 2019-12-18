import json

from django.core.paginator import InvalidPage, Paginator
from django.shortcuts import render, get_object_or_404
from ..models import Category, Post

ITEM_PER_PAGE = 10


def categories_blog(request, template_name="blog/categories.html"):
    page = request.GET.get('page')
    busca = request.GET.get('busca')
    if busca is None:
        paginator = Paginator(Category.objects.all(), ITEM_PER_PAGE)
    else:
        paginator = Paginator(Category.objects.filter(name__icontains=busca), ITEM_PER_PAGE)
    try:
        categorias = paginator.page(page)
    except InvalidPage:
        categorias = paginator.page(1)
    return render(request, template_name, {'categorias': categorias})


def category_detail(request, pk, template_name="blog/category_detail.html"):
    category = get_object_or_404(Category, pk=pk)
    page = request.GET.get('page')
    busca = request.GET.get('busca')
    if busca is None:
        paginator = Paginator(Post.objects.filter(publish=True).filter(categories__in=[category]).distinct(),
                              ITEM_PER_PAGE)
    else:
        paginator = Paginator(Post.objects.filter(title__icontains=busca)
                              .filter(publish=True).filter(categories__in=[category]).distinct(), ITEM_PER_PAGE)
    try:
        posts = paginator.page(page)
    except InvalidPage:
        posts = paginator.page(1)
    return render(request, template_name, {'category': category, 'posts': posts})