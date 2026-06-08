from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)
from .models import Officiant
from .serializers import OfficiantSerializer
from .models import Flower
from .serializers import FlowerSerializer
from rest_framework.permissions import IsAuthenticated
class OfficiantListAPIView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = OfficiantSerializer

    def get_queryset(self):
        search = self.request.GET.get("search")
        if search:
            return Officiant.objects.filter(name__icontains=search)
        return Officiant.objects.all()


class OfficiantDetailAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Officiant.objects.all()
    serializer_class = OfficiantSerializer

class FlowerListAPIView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = FlowerSerializer

    def get_queryset(self):
        search = self.request.GET.get("search")
        if search:
            return Flower.objects.filter(name__icontains=search)
        return Flower.objects.all()
class FlowerDetailAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Flower.objects.all()
    serializer_class = FlowerSerializer