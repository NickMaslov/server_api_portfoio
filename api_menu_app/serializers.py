from rest_framework import serializers
from . import models


class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MenuItem
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    menu_items = MenuItemSerializer(many=True, read_only=True)

    class Meta:
        model = models.Category
        fields = "__all__"


class PlaceDetailSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True, read_only=True)

    class Meta:
        model = models.Place
        fields = "__all__"


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Place
        fields = ["url", "id", "name", "image"]


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Order
        fields = "__all__"
