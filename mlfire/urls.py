from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('accounts/', include('django.contrib.auth.urls')),
    # path('auth/', include('allauth.urls')),
    path('', include('core.urls')),
    # path('accounts/', include('accounts.urls')),
    path('api/', include('api.urls')),
    # path('home/', include('home.urls')),
    # path('general/', include('general.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)