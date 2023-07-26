from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse_lazy, reverse
from django.utils.html import urlencode

from accounts.forms import ProjectUserCreationForm
from webapp.models import Project
from webapp.forms import TodoForm, SearchForm, ProjectForm
from django.http import HttpResponseRedirect,Http404
from django.views.generic import TemplateView, View, FormView, ListView, CreateView, DetailView, DeleteView, UpdateView


# Create your views here.
class ProjectListView(ListView):
    template_name = 'project/project_list.html'
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
        queryset = super().get_queryset()
        if self.search_value:
            queryset = queryset.filter(Q(project_title__icontains=self.search_value) |
                                       Q(project_description__icontains=self.search_value))

        return queryset
class ProjectCreateView(LoginRequiredMixin, CreateView):
    template_name= 'project/create_project.html'
    model = Project
    form_class = ProjectForm


    def get_success_url(self):
        return reverse_lazy('webapp:home')

class ProjectDetailView( DetailView):
    model = Project
    template_name = "project/detail_project.html"




    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["project"] = self.object
        for i in self.object.tasks.all():
            print(i, i.created_date)
        return context

class ProjectDeleteView(LoginRequiredMixin, DeleteView):

    template_name ='project/delete_project.html'

    model = Project

    context_object_name ='project'

    success_url = reverse_lazy('webapp:home')



class ProjectUpdateView(LoginRequiredMixin, UpdateView):

    model = Project

    template_name ='project/update_project.html'

    form_class = ProjectForm

    context_object_name ='project'




    def get_success_url(self):

        return reverse('webapp:detail_project',kwargs={'pk':self.object.pk})

class AddUserProjectView(View):
    def get(self, request, pk):
        project = get_object_or_404(Project, pk=pk)
        form = ProjectUserCreationForm()
        return render(request, 'add_user_to_project.html', {'project': project, 'form': form})

    def post(self, request, pk):
        project = get_object_or_404(Project, pk=pk)
        form = ProjectUserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            user = get_object_or_404(User, username=username)
            project.User_project_name.add(user)
            return redirect('webapp:detail_project', pk=pk)
        return render(request, 'add_user_to_project.html', {'project': project, 'form': form})



