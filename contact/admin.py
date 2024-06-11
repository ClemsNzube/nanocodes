from django.contrib import admin
from .models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'created_at')
    search_fields = ('full_name', 'email')
    list_filter = ('created_at',)
