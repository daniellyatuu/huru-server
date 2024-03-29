from django.contrib import admin
from app.main.models import Article, Category, Testimony, Service


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'sw_title', 'content', 'sw_content', 'active',
                    'belong_to', 'date_posted', 'display_cover_photo_on_view_article']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'sw_name', 'active', 'added_by', 'date_added']


class TestimonyAdmin(admin.ModelAdmin):
    list_display = ['title', 'url', 'content', 'active', 'date_posted']


admin.site.register(Article, ArticleAdmin)
admin.site.register(Testimony, TestimonyAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Service)
