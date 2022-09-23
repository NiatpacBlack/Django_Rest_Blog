from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main_app.urls')),
    path('blog/', include('blog_app.urls')),
    path('contacts/', include('feedback_app.urls')),
    path('registration/', include('registration_app.urls')),
    path('authorization/', include('authorization_app.urls')),
    path('search/', include('search_app.urls')),
]
