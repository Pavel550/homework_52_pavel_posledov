from django.shortcuts import render,redirect
from .models import TODO, TODO_FORM
# Create your views here.
def home(request):
    my_todo = TODO.objects.order_by('id')
    form = TODO_FORM()
    context = {'my_todo': my_todo, 'form': form}
    return render(request, 'todo_list.html', context)


def add_new_todo(request):
    return None


def complete_todo(request):
    return None


def delete_todo(request):
    return None