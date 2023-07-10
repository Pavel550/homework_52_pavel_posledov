from django import forms
from .models import TodoList,TypeTodo,StatusTodo


class StatusTodoForm(forms.Form):
    title = forms.CharField(max_length=50, required=True, label="Название")

class TypeTodoForm(forms.Form):
    title = forms.CharField(max_length=50, required=True, label="Название")







class TodoForm(forms.ModelForm):

    class Meta:
        model = TodoList
        fields = ["title", "status", "type_todo", "short_description", "description"]






