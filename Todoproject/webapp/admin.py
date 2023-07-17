from django.contrib import admin
from .models import TodoList,Project
# Register your models here.
#


class TodoAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'status', 'created_date', ]
    list_display_links = ['id', 'title']
    list_filter = ['status', 'type_todo']
    search_fields = ['title', 'status', 'type_todo']
    fields = ['title', 'status', 'type_todo', 'description', 'short_description']




admin.site.register(TodoList, TodoAdmin)
admin.site.register(Project)