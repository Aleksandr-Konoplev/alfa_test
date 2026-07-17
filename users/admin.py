from django.contrib import admin
from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'is_staff', 'is_superuser', 'is_active', 'date_joined')
    search_fields = ('email',)
    list_filter = ('is_staff', 'is_superuser')
    ordering = ('date_joined',)

