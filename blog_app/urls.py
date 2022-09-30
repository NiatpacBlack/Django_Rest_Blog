from django.urls import path

from . import views


urlpatterns = [
    path('', views.BlogPageView.as_view(), name='blog'),
    path('<url>/', views.PostPageView.as_view(), name='blog_post'),
    path('create_post/', views.CreatePostPageView.as_view(), name='create_post'),
]
