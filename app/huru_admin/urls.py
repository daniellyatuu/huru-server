from django.urls import path
from . import views

app_name = 'huru_admin'

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('article/', views.ArticleView.as_view(), name='article'),
    path('add/', views.AddArticle.as_view(), name='add_article'),
    path('testimony/', views.TestimonyView.as_view(), name='testimony_view'),
    path('add-testimony/', views.AddTestimonyView.as_view(), name='add_testimony'),
    path('service/', views.ServiceView.as_view(), name='service_view'),
    path('add-service/', views.AddServiceView.as_view(), name='add_service'),
]
