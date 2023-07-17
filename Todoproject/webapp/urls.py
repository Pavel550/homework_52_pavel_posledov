from django.urls import path
from webapp.views.todo_views import \
    TodoCreateView,TodoDetailView,TodoListView, TodoDeleteView,TodoUpdateView
from webapp.views.project_views import ProjectListView, ProjectCreateView
urlpatterns = [
    path('', ProjectListView.as_view(), name='home'),
    path('project/create/' , ProjectCreateView.as_view(), name= 'create_project'),
    path('todo/add/', TodoCreateView.as_view(), name='add_todo'),
    path('todo/<int:pk>/detail', TodoDetailView.as_view(), name='detail_todo'),
    path('todo/<int:pk>/delete', TodoDeleteView.as_view(), name = 'delete_todo'),
    path('todo/<int:pk>/update', TodoUpdateView.as_view(), name='todo_update'),

]