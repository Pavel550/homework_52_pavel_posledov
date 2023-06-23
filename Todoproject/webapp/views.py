from django.shortcuts import render
from .models import TodoList
from django.http import HttpResponseRedirect
from datetime import date, datetime
# Create your views here.


def home(request):
    todos = TodoList.objects.order_by("-created_date")
    context = {"todos": todos}
    return render(request, 'todo_list.html', context)


def add_new_todo(request):
    if request.method == "GET":
        return render(request, "add_todolist.html")
    else:
        TodoList.objects.create(
            title=request.POST.get("title"),
            status=request.POST.get("status"),
            description=request.POST.get("description"),
            updated_at=request.POST.get("updated_at"),
            end_date=request.POST.get("end_date".format('d-F-y')),
        )
        return HttpResponseRedirect('/')




def detail_todo(request, *args, pk, **kwargs):
    todo = TodoList.objects.get(id=pk)
    return render(request, "detail_todo.html", {"todo": todo})



def delete_todo(request):
    todo_id = request.GET.get("id")
    todo = TodoList.objects.get(id=todo_id)
    todo.delete()
    return HttpResponseRedirect('/')