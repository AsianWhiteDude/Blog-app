from django.contrib.auth.models import User
from django.db import models







class Posts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    yt_title = models.CharField(max_length=255)
    yt_link = models.URLField()
    content_url = models.URLField(max_length=500)
    time_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.yt_title

    class Meta:
        ordering = ['-time_create']
