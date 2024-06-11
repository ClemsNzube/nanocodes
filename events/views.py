from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Event
from .serializers import EventSerializer
from datetime import date


class EventListCreateView(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]

class EventCategoryListView(generics.ListAPIView):
    serializer_class = EventSerializer

    def get_queryset(self):
        category = self.kwargs['category']
        return Event.objects.filter(category=category)
    

class UpcomingEventListView(generics.ListAPIView):
    serializer_class = EventSerializer

    def get_queryset(self):
        return Event.objects.filter(date__gte=date.today())

