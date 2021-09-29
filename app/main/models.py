from embed_video.fields import EmbedVideoField
from django.contrib.auth.models import Group
from resizeimage import resizeimage
from django.core.files import File
from app.user.models import User
from datetime import datetime
from django.db import models
from io import BytesIO
from PIL import Image
import sys
import os


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

    def pwud_article_list(self):
        return self.category_article.filter(belong_to__name='pwud')

    def hcw_article_list(self):
        return self.category_article.filter(belong_to__name='hcw')


class Article(models.Model):
    user = models.ForeignKey(
        User, related_name='user_article', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    sw_title = models.CharField(max_length=100, blank=True, null=True)
    cover_photo = models.ImageField(upload_to='cover_photo')
    display_cover_photo_on_view_article = models.BooleanField(default=True)
    is_image_compressed = models.BooleanField(default=False)
    content = models.TextField()
    sw_content = models.TextField(blank=True, null=True)
    active = models.BooleanField(default=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='category_article', blank=True, null=True)
    belong_to = models.ForeignKey(
        Group, related_name='article_belong_to', on_delete=models.CASCADE)
    date_posted = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    views = models.PositiveIntegerField(default=0)

    # calling image compression function before saving the data
    def save(self, *args, **kwargs):
        if self.is_image_compressed == False:
            new_image = self.compress(self.cover_photo)
            self.cover_photo = new_image
            self.is_image_compressed = True
        super().save(*args, **kwargs)

    # image compression method
    def compress(self, filename):
        im = Image.open(filename)

        im = im.convert('RGB')

        # get filename extension
        name, ext = os.path.splitext(filename.name)

        ''' new filename '''
        # current date and time
        now = datetime.now()
        timestamp = datetime.timestamp(now)
        new_name = name + str(timestamp)
        new_name = new_name.replace('.', '')

        new_filename = new_name+ext

        # check image size
        width = im.size[0]
        height = im.size[1]

        aspect = width / float(height)

        ideal_width = 800
        ideal_height = 800

        ideal_aspect = ideal_width / float(ideal_height)

        if aspect > ideal_aspect:
            # Then crop the left and right edges:
            new_width = int(ideal_aspect * height)
            offset = (width - new_width) / 2
            resize = (offset, 0, width - offset, height)
        else:
            # ... crop the top and bottom:
            new_height = int(width / ideal_aspect)
            offset = (height - new_height) / 2
            resize = (0, offset, width, height - offset)

        im = im.crop(resize).resize(
            (ideal_width, ideal_height), Image.ANTIALIAS)

        im_io = BytesIO()

        im.save(im_io, 'JPEG', quality=90)
        new_image = File(im_io, name=new_filename)
        return new_image

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
