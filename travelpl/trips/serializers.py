import requests
from rest_framework import serializers
from .models import TravelProject, Place


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = ['id', 'external_id', 'notes', 'is_visited']

    def validate_external_id(self, value):
        api_url = f"https://api.artic.edu/api/v1/artworks/{value}"
        try:
            response = requests.get(api_url, timeout=5)
            if response.status_code != 200:
                raise serializers.ValidationError("Artwork ID not found in Art Institute API.")
        except requests.RequestException:
            raise serializers.ValidationError("API service unavailable.")
        return value


class ProjectSerializer(serializers.ModelSerializer):
    places = PlaceSerializer(many=True, required=False)

    class Meta:
        model = TravelProject
        fields = ['id', 'name', 'description', 'start_date', 'is_completed', 'places']
        read_only_fields = ['is_completed']
        extra_kwargs = {
            'description': {'required': False},
            'start_date': {'required': False, 'allow_null': True},
        }

    def create(self, validated_data):
        places_data = validated_data.pop('places', [])

        # Перевірка ліміту
        if len(places_data) > 10:
            raise serializers.ValidationError({"places": "Maximum 10 places allowed."})

        project = TravelProject.objects.create(**validated_data)
        for place in places_data:
            Place.objects.create(project=project, **place)
        return project