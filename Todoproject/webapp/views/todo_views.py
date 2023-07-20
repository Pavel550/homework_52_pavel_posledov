from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse_lazy, reverse

from webapp.models import TodoList, Project
from webapp.forms import TodoForm
from django.http import HttpResponseRedirect,Http404
from django.views.generic import TemplateView, View, FormView, ListView, CreateView, DetailView, DeleteView, UpdateView


# Create your views here.
class TodoListView(ListView):
    model = TodoList
    template_name = 'todo/todo_list.html'
    context_object_name = 'todos'
    ordering = '-created_date'



class TodoCreateView(CreateView):
    template_name= 'todo/add_todolist.html'
    model = TodoList
    form_class = TodoForm

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return super().dispatch(request, *args, **kwargs)
        return redirect("accounts:login")

    def get_success_url(self):
        return reverse_lazy('webapp:detail_project')





class TodoUpdateView(UpdateView):

    model = TodoList

    template_name ='todo/update_todo.html'

    form_class = TodoForm

    context_object_name ='todo'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return super().dispatch(request, *args, **kwargs)
        return redirect("accounts:login")


    def get_success_url(self):

        return reverse('webapp:detail_project',kwargs={'pk':self.object.project.pk})







class TodoDeleteView(DeleteView):

    model = TodoList

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return super().dispatch(request, *args, **kwargs)
        return redirect("accounts:login")


    def get(self, request, *args, **kwargs):

        return self.delete(request, *args, **kwargs)


    def get_success_url(self):

        return reverse('webapp:detail_project',kwargs={'pk':self.object.project.pk})





class TodoDetailView(DetailView):
    model = TodoList
    template_name = "todo/detail_todo.html"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return super().dispatch(request, *args, **kwargs)
        return redirect("accounts:login")


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tasks"] = self.object
        print(object)
        # for i in self.object.tasks.all():
        #     print(i, i.created_date)
        return context


