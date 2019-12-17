import random

from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.text import slugify


class Post(models.Model):
    slug = models.SlugField('slug', max_length=254, null=False, unique=True, primary_key=True)
    title = models.CharField('Título', max_length=254, null=False)
    content = RichTextUploadingField('Conteúdo', null=False)
    publish = models.BooleanField('Publicar?', null=False, default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if len(self.slug) == 0:
            self.slug = slugify(self.title) + str(random.randint(1,200))
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
