from django.urls import path, include
from api import views
from rest_framework.routers import DefaultRouter
# from general import views as general_views

app_name = 'api'

router = DefaultRouter()
router.register('learnig-models', views.LearnigModelViewSet)
router.register('investigations', views.InvestigationViewSet)
# router.register('profile-photo', views.UploadProfilePhotoViewSet)
# router.register('account/services', account_views.AccountServicesViewSet, basename='account-serviceitem')

urlpatterns = [
    path('', include(router.urls)),
    # path('categories/', views.CategoryListView.as_view(), name='list_categories'),
    # path('general/work-city/', general_views.WorkCityListView.as_view(), name='list_work_city'),
]
