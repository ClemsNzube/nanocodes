from django.urls import path
from .views import AllEventsListView, EventListCreateView, EventCategoryListView, EventDetailView, UpcomingEventListView

urlpatterns = [
    path('events/', EventListCreateView.as_view(), name='event-list-create'),
    path('events/all/', AllEventsListView.as_view(), name='all-events-list'),
    path('events/<int:pk>/', EventDetailView.as_view(), name='event-detail'),
    path('events/category/<str:category>/', EventCategoryListView.as_view(), name='event-category-list'),
    path('upcoming-events/', UpcomingEventListView.as_view(), name='upcoming-event-list'),
]
