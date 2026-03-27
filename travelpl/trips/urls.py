from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet, PlaceViewSet

router = DefaultRouter()
router.register('project', ProjectViewSet)
router.register('place', PlaceViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('project/<int:project_id>/places/', PlaceViewSet.as_view({'get': 'list_by_project'})),
    path('project/<int:project_id>/places/<int:pk>/', PlaceViewSet.as_view({'get': 'retrieve'})),
]
