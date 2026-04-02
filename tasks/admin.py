from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'priority', 'is_slayed', 'due_date', 'created_at']
    list_filter  = ['is_slayed', 'priority', 'user']
    search_fields = ['title', 'description']
