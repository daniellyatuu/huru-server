from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from django.urls import path, include


urlpatterns = [
    path('', include('app.main.urls', namespace='main')),
    path('api/', include('app.main.api.urls', namespace='main_api')),
    path('auth/', include('app.user.urls')),
    path('admin/', include('app.huru_admin.urls')),
    path('super-admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
admin.site.site_header = 'Huru adminstration'
admin.site.site_title = 'Huru'
