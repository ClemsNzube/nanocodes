from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from .models import CustomUser

class CustomUserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('email', 'phone_number')}),
        ('Permissions', {'fields': ('is_admin', 'is_staff', 'is_superuser', 'is_active', 'email_verified')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'phone_number', 'password1', 'password2'),
        }),
    )
    list_display = ('username', 'email', 'phone_number', 'is_admin', 'is_staff', 'is_superuser', 'email_verified')
    list_filter = ('is_admin', 'is_staff', 'is_superuser', 'email_verified')
    search_fields = ('username', 'email', 'phone_number')
    ordering = ('username',)
    filter_horizontal = ()

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.unregister(Group)
