from django.contrib import admin
from app.main.models import Article, Category, Testimony


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'content',
                    'active', 'belong_to', 'date_posted']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'active', 'added_by', 'date_added']


class TestimonyAdmin(admin.ModelAdmin):
    list_display = ['title', 'url', 'content', 'active', 'date_posted']


admin.site.register(Article, ArticleAdmin)
admin.site.register(Testimony, TestimonyAdmin)
admin.site.register(Category, CategoryAdmin)
