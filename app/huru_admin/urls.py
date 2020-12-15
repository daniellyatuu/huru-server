from django.urls import path
from . import views

app_name = 'huru_admin'

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('article/', views.ArticleView.as_view(), name='article'),
    path('add/', views.AddArticle.as_view(), name='add_article'),
    path('testimony/', views.TestimonyView.as_view(), name='testimony_view'),
    path('add-testimony/', views.AddTestimonyView.as_view(), name='add_testimony'),
]
