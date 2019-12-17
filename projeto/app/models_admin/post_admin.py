from django.contrib import admin
from ..forms import PostForm


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'publish', 'user', 'created_at', 'updated_at']
    search_fields = ('title',)
    list_editable = ['publish']
    list_filter = ('publish', 'user', 'categories')
    form = PostForm

    fieldsets = [
        ("Título e publicação", {'fields': (tuple(['title', 'publish']),), }),
        ("Conteúdo", {'fields': ['content']}),
        ("Categorias", {'fields': ['categories']})
    ]

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()
