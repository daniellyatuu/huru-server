# Generated by Django 3.1.2 on 2022-05-13 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_article_is_image_compressed'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='sw_name',
            field=models.CharField(blank=True, max_length=255, null=True, unique=True),
        ),
    ]