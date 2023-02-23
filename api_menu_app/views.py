from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from . import models, serializers

# Create your views here.
class PlaceViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.PlaceSerializer
    queryset = models.Place.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
