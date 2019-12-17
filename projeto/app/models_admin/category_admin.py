from django.contrib import admin
from ..forms import CategoryForm


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')
    search_fields = ('name',)

    fieldsets = (
        (None, {
            'fields': ('name',)
        }),
    )
    form = CategoryForm
