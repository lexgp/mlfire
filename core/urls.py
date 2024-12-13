from django.urls import path, include
from core import views
from rest_framework.routers import DefaultRouter

app_name = 'core'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home-view'),
]