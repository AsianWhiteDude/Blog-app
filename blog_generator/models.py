from django.db import models
from django.urls import reverse, reverse_lazy


class Posts(models.Model):
    title = models.CharField(blank=False, max_length=255)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-time_create']

    def get_absolute_url(self):
        return reverse_lazy('post', kwargs={'post_slug': self.slug})