# Generated by Django 3.1.2 on 2021-02-05 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_article_display_cover_photo_on_view_article'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='sw_content',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='sw_title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]