# Generated by Django 3.1.2 on 2020-12-28 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20201217_1822'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facility', models.CharField(max_length=255)),
                ('facility_type', models.CharField(max_length=255)),
                ('service_offered', models.CharField(max_length=255)),
                ('contact', models.CharField(max_length=17)),
                ('region', models.CharField(max_length=50)),
                ('district', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
