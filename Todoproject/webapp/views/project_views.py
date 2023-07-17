from django.db.models import Q
from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse_lazy
from django.utils.html import urlencode

from webapp.models import Project
from webapp.forms import TodoForm, SearchForm, ProjectForm
from django.http import HttpResponseRedirect,Http404
from django.views.generic import TemplateView, View, FormView, ListView, CreateView


# Create your views here.
class ProjectListView(ListView):
    template_name = 'PROJECT/project_list.html'
    context_object_name = 'projects'
    paginate_by = 5
    paginate_orphans = 1
    model = Project


    def dispatch(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context['form'] = self.form
        if self.search_value:
            context['query'] = urlencode({'search': self.search_value})
            context['search_value'] = self.search_value
        return context

    def get_search_form(self):
        return SearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search']
        else:
            return None

    def get_queryset(self):
        # return Project.objects.all().order_by('-project_created_date')
        queryset = super().get_queryset()
        if self.search_value:
            queryset = queryset.filter(Q(project_title__icontains=self.search_value) |
                                       Q(todo_title__icontains=self.search_value))

        return queryset
class ProjectCreateView(CreateView):
    template_name= 'PROJECT/create_project.html'
    model = Project
    form_class = ProjectForm


    def get_success_url(self):
        return reverse_lazy('home')


#
#
# class TodoUpdateView(FormView):
#     form_class = TodoForm
#     template_name = "TODO/update_todo.html"
#     def dispatch(self, request, *args, **kwargs):
#         self.todo = self.get_object(kwargs.get("pk"))
#         return super().dispatch(request, *args, **kwargs)
#
#     def get_object(self, pk):
#         return get_object_or_404(TodoList, id=pk)
#
#
#     def get_initial(self):
#         initial = {}
#         for key in 'title', 'status', 'type_todo', 'short_description', 'description':
#             initial[key] = getattr(self.todo, key)
#         initial['type_todo'] = self.todo.type_todo.all()
#         return initial
#
#
#     def form_valid(self, form):
#         type_todo = form.cleaned_data.pop("type_todo")
#         for key, value in form.cleaned_data.items():
#             if value is not None:
#                 setattr(self.todo, key, value)
#         self.todo.save()
#         self.todo.type_todo.set(type_todo)
#         return redirect("home")
#
#
#
# class TodoDeleteView(TemplateView):
#     def get(self, request, *args, **kwargs):
#         todo = get_object_or_404(TodoList, id=kwargs['pk'])
#         return render(request, "TODO/delete_todo.html", {"todo": todo})
#
#
#     def post(self,*args,**kwargs):
#         todo = get_object_or_404(TodoList,id=kwargs['pk'])
#         todo.delete()
#         return redirect('home')
#
#     def get_template_names(self,**kwargs):
#         return "delete_todo.html"
#
#
#
# class TodoDetailView(TemplateView):
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["todo"] = get_object_or_404(TodoList, id=kwargs['pk'])
#         return context
#     def get_template_names(self):
#         return "detail_todo.html"