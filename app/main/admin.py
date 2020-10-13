from django.contrib import admin
from app.main.models import Article, Testimony


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'content',
                    'active', 'belong_to', 'date_posted']


class TestimonyAdmin(admin.ModelAdmin):
    list_display = ['title', 'url', 'content', 'active', 'date_posted']


admin.site.register(Article, ArticleAdmin)
admin.site.register(Testimony, TestimonyAdmin)
