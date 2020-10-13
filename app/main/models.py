from django.contrib.auth.models import Group
from app.user.models import User
from django.db import models


class Article(models.Model):
    user = models.ForeignKey(
        User, related_name='user_article', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    cover_photo = models.ImageField(upload_to='cover_photo')
    content = models.TextField()
    active = models.BooleanField(default=True)
    belong_to = models.ForeignKey(
        Group, related_name='article_belong_to', on_delete=models.CASCADE)
    date_posted = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return '{}'.format(self.title)


class Testimony(models.Model):
    title = models.CharField(max_length=255)
    url = models.CharField(max_length=100)
    content = models.TextField(blank=True, null=True)
    active = models.BooleanField(default=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-id']
        verbose_name_plural = 'Testimony'

    def __str__(self):
        return '{}'.format(self.title)
