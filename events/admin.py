from django.contrib import admin
from .models import Event, Category

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'event_time', 'location')
    search_fields = ('name', 'location')
    list_filter = ('date',)
    date_hierarchy = 'date'

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)