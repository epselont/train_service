from django.contrib import admin
from models import User


@admin.register(User)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'role')
    search_fields = ('username',)
    list_filter = ('username', 'email')
    empty_value_display = '-пусто-'
