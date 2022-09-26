from django.urls import path
from . import views


urlpatterns = [
    path('', views.BlogPageView.as_view(), name='blog'),
    path('<url>/', views.PostPageView.as_view(), name='blog_post'),
]
