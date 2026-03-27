from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet, PlaceViewSet

router = DefaultRouter()
router.register('project', ProjectViewSet)
router.register('place', PlaceViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
