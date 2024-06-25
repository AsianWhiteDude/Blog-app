from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls', namespace='users')),
    path('', include('blog_generator.urls')),
]

urlpatterns = urlpatterns+static(settings.MEDIA_ROOT, document_root=settings.MEDIA_ROOT)