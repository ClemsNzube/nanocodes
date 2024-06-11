from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from .models import Event
from .serializers import EventSerializer
from datetime import date

class EventListCreateView(generics.ListCreateAPIView):
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Event.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class EventDetailView(generics.RetrieveDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        event = self.get_object()
        if event.owner != request.user:
            raise PermissionDenied("You do not have permission to delete this event.")
        return super().delete(request, *args, **kwargs)

class EventCategoryListView(generics.ListAPIView):
    serializer_class = EventSerializer

    def get_queryset(self):
        category = self.kwargs['category']
        return Event.objects.filter(categories__name=category)

class UpcomingEventListView(generics.ListAPIView):
    serializer_class = EventSerializer

    def get_queryset(self):
        return Event.objects.filter(date__gte=date.today())
    
class AllEventsListView(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.AllowAny]
