from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('article/', views.ArticleView.as_view(), name='article_list'),
    path('service/', views.ServiceView.as_view(), name='service_list'),
]
