from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from . import models, serializers

# Create your views here.
class PlaceViewSet(viewsets.ModelViewSet):
    queryset = models.Place.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.action == "list":
            return serializers.PlaceSerializer
        else:
            return serializers.PlaceDetailSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CategorySerializer
    queryset = models.Category.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]


class MenuItemViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.MenuItemSerializer
    queryset = models.MenuItem.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]


class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.OrderSerializer
    queryset = models.Order.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
