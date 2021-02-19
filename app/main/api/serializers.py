from rest_framework import serializers
from app.main.models import Article, Service


class ArticleSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username')
    category = serializers.CharField(source='category.name')

    class Meta:
        model = Article
        fields = ['id', 'user', 'title', 'sw_title', 'cover_photo',
                  'display_cover_photo_on_view_article', 'content', 'sw_content', 'category', 'date_posted']


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['facility', 'facility_type', 'service_offered',
                  'contact', 'region', 'district', 'location']
