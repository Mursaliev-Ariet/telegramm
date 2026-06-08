from rest_framework import serializers
from .models import Clothes, Officiant, Flower


class ClothesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clothes
        fields = "__all__"


class OfficiantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Officiant
        fields = "__all__"


class FlowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flower
        fields = "__all__"