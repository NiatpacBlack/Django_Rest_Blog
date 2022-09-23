from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_page, name='blog'),
    path('1/', views.blog_post_page, name='blog_post'),
]
