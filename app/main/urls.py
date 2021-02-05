from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('hcw/', views.HCWHomeView.as_view(), name='hcw_home'),
    path('about-us/', views.AboutUsView.as_view(), name='about_us'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('testimony/', views.TestimonyView.as_view(), name='testimony'),
    path('blog/', views.BlogView.as_view(), name='blog'),
    path('hcw-blog/', views.HcwBlogView.as_view(), name='hcw_blog'),
    path('blog-detail/<int:pk>/', views.BlogDetailView.as_view(), name='blog_detail'),
    path('hcw-blog-detail/<int:pk>/', views.HcwBlogDetailView.as_view(), name='hcw_blog_detail'),
    path('category-info/<int:pk>', views.CategoryDetailView.as_view(),
         name='category_information'),
     path('hcw-category-info/<int:pk>', views.HcwCategoryDetailView.as_view(),
         name='hcw_category_information'),
    path('services/', views.ServiceView.as_view(), name='service_list'),
    path('testimony-detail/<int:pk>/',
         views.TestimonyDetailView.as_view(), name='testimony_detail'),
    path('privacy-policy/', views.PrivacyPolicy.as_view(), name='privacy_policy'),
]
