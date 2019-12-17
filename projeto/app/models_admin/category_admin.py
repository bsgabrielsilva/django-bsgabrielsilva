from django.contrib import admin
from ..forms import CategoryForm


class CategoryAdmin(admin.ModelAdmin):
    form = CategoryForm
