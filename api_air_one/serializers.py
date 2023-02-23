from rest_framework import serializers
from . import models


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.City
        fields = "__all__"


class PlaneSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Plane
        fields = "__all__"


class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Route
        fields = "__all__"
