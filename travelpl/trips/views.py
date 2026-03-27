from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import TravelProject, Place
from .serializers import ProjectSerializer, PlaceSerializer
from rest_framework.exceptions import ValidationError

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = TravelProject.objects.all()
    serializer_class = ProjectSerializer

    def destroy(self, request, *args, **kwargs):
        project = self.get_object()
        if project.places.filter(is_visited=True).exists():
            return Response("error, Не можна видалити проект де вже відвідані місця", status=status.HTTP_400_BAD_REQUEST)
        return super().destroy(request, *args, **kwargs)

class PlaceViewSet(viewsets.ModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer

    def perform_create(self, serializer):
        project_id = self.request.data.get('project')
        project = TravelProject.objects.get(pk=project_id)

        if project.places.count() > 10:
            raise ValidationError('Максимум 10 місць у проекті')

        instance = serializer.save(project=project)
        instance.project.update_completion_status()

    def perform_update(self, serializer):
        instance = serializer.save()
        instance.project.update_completion_status()