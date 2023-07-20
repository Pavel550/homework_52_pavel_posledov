from django.urls import path

from webapp.views.project_tasks_views import ProjectTasksCreateView
from webapp.views.todo_views import \
    TodoCreateView,TodoDetailView,TodoListView, TodoDeleteView,TodoUpdateView
from webapp.views.project_views import ProjectListView, ProjectCreateView, ProjectDetailView, ProjectDeleteView, \
    ProjectUpdateView

app_name = "webapp"

urlpatterns = [
    path('', ProjectListView.as_view(), name='home'),
    path('project/create/' , ProjectCreateView.as_view(), name= 'create_project'),
    path('project/<int:pk>/detail', ProjectDetailView.as_view(), name= 'detail_project'),
    path('project/<int:pk>/todo/add', ProjectTasksCreateView.as_view(), name='add_todo'),
    path('project/<int:pk>/delete/', ProjectDeleteView.as_view(), name='delete_project'),
    path('project/<int:pk>/update', ProjectUpdateView.as_view(), name='project_update'),
    path('todo/<int:pk>/detail', TodoDetailView.as_view(), name='detail_todo'),
    path('todo/<int:pk>/delete', TodoDeleteView.as_view(), name = 'delete_todo'),
    path('todo/<int:pk>/update', TodoUpdateView.as_view(), name='todo_update'),

]