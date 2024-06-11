from django.contrib import admin
from .models import Event, Category

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'event_time', 'start_time', 'end_time', 'location', 'owner')
    search_fields = ('name', 'location', 'owner__username')
    list_filter = ('date', 'categories')
    ordering = ('date',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
