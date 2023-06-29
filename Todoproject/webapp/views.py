from django.shortcuts import render,redirect,get_object_or_404
from .models import TodoList
from django.http import HttpResponseRedirect,Http404

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
        return redirect("home")




def detail_todo(request, *args, pk, **kwargs):
    try:
        todo = TodoList.objects.get(id=pk)
    except TodoList.DoesNotExist:
        raise Http404()
    return render(request, "detail_todo.html", {"todo": todo})

def todo_update(request, pk):
    todo = get_object_or_404(TodoList, pk=pk)
    if request.method == "GET":
        return render(request, "update_todo.html", context={'todo': todo})
    elif request.method == 'POST':
        todo.title=request.POST.get("title")
        todo.status=request.POST.get("status")
        todo.description=request.POST.get("description")
        todo.updated_at=request.POST.get("updated_at")
        todo.end_date=request.POST.get("end_date".format('d-F-y'))
        todo.save()

        return redirect("home")



def delete_todo(request, pk):
    # todo_id = request.GET.get("id")
    todo = TodoList.objects.get(id=pk)
    todo.delete()
    return HttpResponseRedirect('/')