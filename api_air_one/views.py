from rest_framework.permissions import BasePermission, SAFE_METHODS


from . import models, serializers

from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

# Custom permission
class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS or request.user.is_staff


class CityViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CitySerializer
    queryset = models.City.objects.all()
    permission_classes = [IsAdminOrReadOnly]


class PlaneViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.PlaneSerializer
    queryset = models.Plane.objects.all()
    permission_classes = [IsAdminOrReadOnly]


class RouteViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.RouteSerializer
    queryset = models.Route.objects.all()
    permission_classes = [IsAdminOrReadOnly]
    # def get_permissions(self):
    #     if self.action in ["list", "retrieve"]:
    #         permission_classes = []
    #     else:
    #         permission_classes = [IsAdminUser]
    #     return [permission() for permission in permission_classes]


def find_routes():
    """
    POST request using Dijkstra graph algorithm
    """
    pass

    # def get_permissions(self):
    #     if self.action in ["list", "retrieve"]:
    #         permission_classes = []
    #     else:
    #         permission_classes = [IsAdminUser]
    #     return [permission() for permission in permission_classes]
