from django.urls import path
from . import views

urlpatterns = [
    path('', views.BlogPageView.as_view(), name='blog'),
    path('1/', views.blog_post_page, name='blog_post'),
]
