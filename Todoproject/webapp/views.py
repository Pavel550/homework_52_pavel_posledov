from django.shortcuts import render,redirect,get_object_or_404
from .models import TodoList
from .forms import TodoForm
from django.http import HttpResponseRedirect,Http404
from django.views.generic import TemplateView,View

# Create your views here.
class TodoListWiew(TemplateView):
    def get(self, request, *args, **kwargs):

        todos = TodoList.objects.order_by("-created_date")
        context = {"todos": todos}
        return render(request, 'todo_list.html', context)

class TodoCreateView(View):
    def get(self, request, *args, **kwargs):
        form = TodoForm()
        return render(request, "add_todolist.html", {'form': form})
    def post(self,request, *args, **kwargs):
            form = TodoForm(data=request.POST)
            if form.is_valid():
                todo = TodoList.objects.create(
                    title=form.cleaned_data.get('title'),
                    status=form.cleaned_data.get('status'),
                    type_todo=form.cleaned_data.get('type_todo'),
                    short_description=form.cleaned_data.get('short_description'),
                    description=form.cleaned_data.get('description'),)
                todo.save()
                return redirect('home')
            else:
                return redirect(request, "add_todolist.html", {'form':form})
class TodoUpdateView(View):
    def get(self,request, *args,**kwargs):
        todo = get_object_or_404(TodoList, id=kwargs['pk'])
        form = TodoForm(initial={
            "title": todo.title,
            "status": todo.status,
            "type_todo": todo.type_todo,
            "short_description": todo.short_description,
            "description": todo.description
        })
        return render(request, "update_todo.html", {'form': form})

    def post(self,request,*args,**kwargs):
            todo = get_object_or_404(TodoList, id=kwargs['pk'])
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

class TodoDeleteView(TemplateView):
    def get(self, request, *args, **kwargs):
        todo = get_object_or_404(TodoList, id=kwargs['pk'])
        return render(request, "delete_todo.html", {"todo": todo})


    def post(self,*args,**kwargs):
        todo = get_object_or_404(TodoList,id=kwargs['pk'])
        todo.delete()
        return redirect('home')

    def get_template_names(self,**kwargs):
        return "delete_todo.html"



class TodoDetailView(TemplateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["todo"] = get_object_or_404(TodoList, id=kwargs['pk'])
        return context
    def get_template_names(self):
        return "detail_todo.html"