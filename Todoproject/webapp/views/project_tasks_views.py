from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import CreateView

from webapp.forms import TodoForm
from webapp.models import TodoList, Project


class ProjectTasksCreateView(CreateView):
    model = TodoList

    form_class = TodoForm

    template_name ='todo/add_todolist.html'


    def form_valid(self, form):

        project = get_object_or_404(Project,pk=self.kwargs.get('pk'))

        form.instance.project = project

        return super().form_valid(form)


    def get_success_url(self):

        # также pk можно получить, как self.kwargs.get('pk')

        return reverse('detail_project',kwargs={'pk':self.object.project.pk})


