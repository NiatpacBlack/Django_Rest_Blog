from django.urls import path
from . import views

urlpatterns = [
    path('', views.authorization_page, name='authorization'),
]
