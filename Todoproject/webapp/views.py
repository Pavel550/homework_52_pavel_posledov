from django.shortcuts import render,redirect,get_object_or_404
from .models import TodoList
from .forms import TodoForm
from django.http import HttpResponseRedirect,Http404

# Create your views here.


def home(request):
    todos = TodoList.objects.order_by("-created_date")
    context = {"todos": todos}
    return render(request, 'todo_list.html', context)


def add_new_todo(request):
    if request.method == "GET":
        form = TodoForm()
        return render(request, "add_todolist.html", {'form': form})
    elif request.method == "POST":
        form = TodoForm(data=request.POST)
        if form.is_valid():
            todo = TodoList(
                title=form.cleaned_data.get('title'),
                status=form.cleaned_data.get('status'),
                type_todo=form.cleaned_data.get('type_todo'),
                short_description=form.cleaned_data.get('short_description'),
                description=form.cleaned_data.get('description'),
                created_date=form.cleaned_data.get('created_date'),
                updated_at=form.cleaned_data.get('updated_at')


            )
            todo.save()
            return redirect('home')
        else:
            return redirect(request, "add_todolist.html", {'form':form})




def detail_todo(request, *args, pk, **kwargs):
    try:
        todo = TodoList.objects.get(id=pk)
    except TodoList.DoesNotExist:
        raise Http404()
    return render(request, "detail_todo.html", {"todo": todo})

def todo_update(request, pk):
    todo = get_object_or_404(TodoList, id=pk)
    form = TodoForm(initial={
        "title": todo.title,
        "status": todo.status,
        "type_todo": todo.type_todo,
        "short_description": todo.short_description,
        "description": todo.description
    })
    if request.method == "GET":
        return render(request, "update_todo.html", {'form': form})
    elif request.method == 'POST':
        form = TodoForm(data=request.POST)
        if form.is_valid():
            todo.title=form.cleaned_data.get("title")
            todo.status=form.cleaned_data.get("status")
            todo.type_todo=form.cleaned_data.get("type_todo")
            todo.short_description=form.cleaned_data.get("short_description")
            todo.description=form.cleaned_data.get("description")
            todo.save()
            return redirect('home')
        else:
            return render(request, "update_todo.html", {'form': form})



def delete_todo(request, pk):
    todo = get_object_or_404(TodoList,id=pk)
    if request.method == 'GET':
        return render(request, 'delete_todo.html', {'todo': todo})
    elif request.method == 'POST':
        todo.delete()
    return redirect('home')