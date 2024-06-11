from django.urls import path
from .views import AllEventsListView, CategoryListCreateView, EventListCreateView, EventCategoryListView, EventDetailView, UpcomingEventListView

urlpatterns = [
    path('', EventListCreateView.as_view(), name='event-list-create'),
    path('all/', AllEventsListView.as_view(), name='all-events-list'),
    path('<int:pk>/', EventDetailView.as_view(), name='event-detail'),
    path('category/<int:category_id>/', EventCategoryListView.as_view(), name='event-category-list'),
    path('upcoming-events/', UpcomingEventListView.as_view(), name='upcoming-event-list'),
    path('categories/', CategoryListCreateView.as_view(), name='category-list-create'),

]
