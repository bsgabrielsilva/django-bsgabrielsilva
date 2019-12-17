from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    slug = models.SlugField('slug', max_length=254, null=False, unique=True, primary_key=True)
    name = models.CharField('Name', max_length=254, null=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if len(self.slug) == 0:
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name_plural = "Categories"
