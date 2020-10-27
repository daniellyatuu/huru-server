from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('login/', views.UserLogin.as_view(), name='login'),
    path('logout/', views.UserLogout.as_view(), name='logout'),
]
