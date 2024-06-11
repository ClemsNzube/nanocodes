from rest_framework import generics, permissions
from rest_framework.exceptions import ValidationError
from .models import Rating
from rest_framework.exceptions import PermissionDenied
from .serializers import RatingSerializer

class RatingListCreateView(generics.ListCreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user

        if Rating.objects.filter(user=user).exists():
            raise ValidationError('You have already rated the platform.')

        serializer.save(user=user)

class RatingDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        if self.request.user != serializer.instance.user:
            raise PermissionDenied("You do not have permission to edit this rating.")
        serializer.save()

    def perform_destroy(self, instance):
        if self.request.user != instance.user:
            raise PermissionDenied("You do not have permission to delete this rating.")
        instance.delete()
