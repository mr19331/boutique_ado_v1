from .import views
from django.urls import path


urlpatterns = [
    path('', views.PostList, name='blog'),
    ]

