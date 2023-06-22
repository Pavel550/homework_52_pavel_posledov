from django.contrib import admin
from .models import TodoList
# Register your models here.
#


class TodoAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'status', 'created_date', 'end_date']
    list_display_links = ['id', 'title']
    list_filter = ['status']
    search_fields = ['title', 'status']
    fields = ['title', 'status', 'description', 'end_date']




admin.site.register(TodoList, TodoAdmin)