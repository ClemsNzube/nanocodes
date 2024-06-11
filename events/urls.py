from django.urls import path
from .views import EventListCreateView, EventCategoryListView, UpcomingEventListView

urlpatterns = [
    path('events/', EventListCreateView.as_view(), name='event-list-create'),
    path('events/<str:category>/', EventCategoryListView.as_view(), name='event-category-list'),
    path('upcoming-events/', UpcomingEventListView.as_view(), name='upcoming-event-list'),

]
