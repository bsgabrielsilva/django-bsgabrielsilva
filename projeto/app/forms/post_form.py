from django import forms
from ..models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'publish', 'categories']
        widgets = {
            'title': forms.TextInput(),
            'content': forms.Textarea(),
            'publish': forms.CheckboxInput(),
            'categories': forms.SelectMultiple()
        }

        help_texts = {
            'title': 'Informe um título',
            'content': 'Escreva o conteúdo',
            'publish': 'Publicar?',
            'categories': 'Informe as categorias'
        }