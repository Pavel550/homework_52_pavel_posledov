from django.contrib import admin
from .models import TodoList
# Register your models here.
#


class TodoAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_at']
    list_display_links = ['id', 'title']
    search_fields = ['title', 'content']
    fields = ['title', 'content', 'created_at']
    readonly_fields = ['created_at']




admin.site.register(TodoList, TodoAdmin)