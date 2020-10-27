from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from django.urls import path, include


urlpatterns = [
    path('', include('app.main.urls')),
    path('user/', include('app.user.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
admin.site.site_header = 'Huru adminstration'
