from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from . import models, serializers

# Create your views here.
class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ProductSerializer
    queryset = models.Product.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
