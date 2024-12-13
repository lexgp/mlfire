from django.urls import path, include
from core import views
from rest_framework.routers import DefaultRouter

app_name = 'core'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home-view'),
    # path('index-auth/', views.HomeAuthView.as_view(), name='home-auth-view'),
    # path('search/', views.SearchView.as_view(), name='search-view'),
    # path('service/', views.ServiceView.as_view(), name='service-view'),

    # path('about_company/', views.AboutCompanyView.as_view(), name='about-company-view'),
    # path('faq/', views.FaqView.as_view(), name='icons-view'),
    # path('news/', views.NewsView.as_view(), name='icons-view'),
    # path('post/', views.PostView.as_view(), name='icons-view'),

    # path('categories/tree/', views.CategoryTreeView.as_view(), name='category-tree-list'),

]