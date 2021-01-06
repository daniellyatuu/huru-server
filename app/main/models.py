from django.contrib.auth.models import Group
from app.user.models import User
from django.db import models
from embed_video.fields import EmbedVideoField


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    active = models.BooleanField(default=True)
    added_by = models.ForeignKey(
        User, related_name='user_category', on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'category'
        ordering = ['-id']
        verbose_name_plural = 'categories'

    def article_list(self):
        return self.category_article.all()


class Article(models.Model):
    user = models.ForeignKey(
        User, related_name='user_article', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    cover_photo = models.ImageField(upload_to='cover_photo')
    content = models.TextField()
    active = models.BooleanField(default=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='category_article', blank=True, null=True)
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
    url = EmbedVideoField()
    content = models.TextField(blank=True, null=True)
    active = models.BooleanField(default=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-id']
        verbose_name_plural = 'Testimony'

    def __str__(self):
        return '{}'.format(self.title)


class Service(models.Model):
    facility = models.CharField(max_length=255)
    facility_type = models.CharField(max_length=255)
    service_offered = models.TextField()
    contact = models.CharField(max_length=17)
    region = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    location = models.CharField(max_length=100)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.facility
