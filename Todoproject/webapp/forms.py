from django import forms
from django.core.exceptions import ValidationError

from .models import TodoList, TypeTodo, StatusTodo, Project


def at_least_10(value):
    if len(value)<10:
        raise ValidationError('Это значение слишком короткое')

def len_50(value):
    if len(value)>50:
        raise ValidationError('Это значение слишком длинное')

class StatusTodoForm(forms.Form):
    title = forms.CharField(max_length=50, required=True, label="Название")

class TypeTodoForm(forms.Form):
    title = forms.CharField(max_length=50, required=True, label="Название")


class SearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label='Найти')



class TodoForm(forms.ModelForm):
    title = forms.CharField(max_length=50, required=True, label='Название', validators=[at_least_10])
    short_description = forms.CharField(max_length=50, required=True, label='Заголовок', validators=[len_50])

    class Meta:
        model = TodoList
        fields = ["title", "status", "type_todo", "short_description", "description"]


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['project_title', 'project_description', 'project_created_date', 'project_finish_date']

        widgets = {
            'project_created_date': forms.DateInput(attrs={'type': 'date'}),
            'project_finish_date': forms.DateInput(attrs={'type': 'date'})
        }