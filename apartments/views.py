from rest_framework import viewsets, permissions
from .models import Apartment
from .serializers import ApartmentSerializer

class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user

class ApartmentViewSet(viewsets.ModelViewSet):
    queryset = Apartment.objects.all()
    permission_classes = [permissions.IsAuthenticated, IsOwner]
    serializer_class = ApartmentSerializer

    def get_queryset(self):
        return Apartment.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
