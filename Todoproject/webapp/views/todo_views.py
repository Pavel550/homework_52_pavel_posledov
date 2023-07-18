from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse_lazy

from webapp.models import TodoList, Project
from webapp.forms import TodoForm
from django.http import HttpResponseRedirect,Http404
from django.views.generic import TemplateView, View, FormView, ListView, CreateView


# Create your views here.
class TodoListView(ListView):
    model = TodoList
    template_name = 'todo/todo_list.html'
    context_object_name = 'todos'
    ordering = '-created_date'


    # def get(self, request, *args, **kwargs):
    #
    #     todos = TodoList.objects.order_by("-created_date")
    #     context = {"todos": todos}
    #     return render(request, 'todo/todo_list.html', context)

class TodoCreateView(CreateView):
    template_name= 'todo/add_todolist.html'
    model = TodoList
    form_class = TodoForm

    def get_success_url(self):
        return reverse_lazy('detail_project')




    # def form_valid(self, form):
    #     type_todo = form.cleaned_data.pop("type_todo")
    #     todo = TodoList.objects.create(
    #         title=form.cleaned_data.get('title'),
    #         status=form.cleaned_data.get('status'),
    #         short_description=form.cleaned_data.get('short_description'),
    #         description=form.cleaned_data.get('description'), )
    #     todo.type_todo.set(type_todo)
    #     return super().form_valid(form)


class TodoUpdateView(FormView):
    form_class = TodoForm
    template_name = "todo/update_todo.html"
    def dispatch(self, request, *args, **kwargs):
        self.todo = self.get_object(kwargs.get("pk"))
        return super().dispatch(request, *args, **kwargs)

    def get_object(self, pk):
        return get_object_or_404(TodoList, id=pk)


    def get_initial(self):
        initial = {}
        for key in 'title', 'status', 'type_todo', 'short_description', 'description':
            initial[key] = getattr(self.todo, key)
        initial['type_todo'] = self.todo.type_todo.all()
        return initial


    def form_valid(self, form):
        type_todo = form.cleaned_data.pop("type_todo")
        for key, value in form.cleaned_data.items():
            if value is not None:
                setattr(self.todo, key, value)
        self.todo.save()
        self.todo.type_todo.set(type_todo)
        return redirect("home")



class TodoDeleteView(TemplateView):
    def get(self, request, *args, **kwargs):
        todo = get_object_or_404(TodoList, id=kwargs['pk'])
        return render(request, "todo/delete_todo.html", {"todo": todo})


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