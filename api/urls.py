from django.urls import path, include
from api import views
from rest_framework.routers import DefaultRouter

app_name = 'api'

router = DefaultRouter()
router.register('learnig-models', views.LearnigModelViewSet)
router.register('investigations', views.InvestigationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
