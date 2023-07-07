from django import forms
from .models import TodoList,TypeTodo,StatusTodo


class StatusTodoForm(forms.Form):
    title = forms.CharField(max_length=50, required=True, label="Название")

class TypeTodoForm(forms.Form):
    title = forms.CharField(max_length=50, required=True, label="Название")







class TodoForm(forms.Form):
    title = forms.CharField(max_length=50, required=True, label="Название")
    description = forms.CharField(max_length=2000, required=False, label="Описание")
    status = forms.ModelChoiceField(queryset=StatusTodo.objects.all(),required=True, label="статус")
    type_todo = forms.ModelChoiceField(queryset=TypeTodo.objects.all(), required=True, label="тип")
    short_description= forms.CharField(max_length=100, required=True, label="Заголовок")


