from django.contrib import admin
from .models import Rating

@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('user', 'stars', 'created_at')
    search_fields = ('user__username',)
    list_filter = ('stars', 'created_at')
