from django.shortcuts import render
from .models import TodoList
from django.http import HttpResponseRedirect
# Create your views here.


def home(request):
    todo = TodoList.objects.order_by("created_at")
    context = {"todo": todo}
    return render(request, 'todo_list.html', context)


def add_new_todo(request):
    if request.method == "GET":
        return render(request, "add_todolist.html")
    else:
        TodoList.objects.create(
            title=request.POST.get("title"),
            content=request.POST.get("content")
        )
        return HttpResponseRedirect('/')




def detail_todo(request):
    todo_id = request.GET.get("id")
    todo = TodoList.objects.get(id=todo_id)
    return render(request, "detail_todo.html", {"todo": todo})



def delete_todo(request):
    TodoList.objects.filter(complete=True).delete()
    return HttpResponseRedirect('/')