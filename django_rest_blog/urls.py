from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main_app.urls')),
    path('blog/', include('blog_app.urls')),
    path('contacts/', include('feedback_app.urls')),
    path('registration/', include('registration_app.urls')),
    path('authorization/', include('authorization_app.urls')),
    path('search/', include('search_app.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
