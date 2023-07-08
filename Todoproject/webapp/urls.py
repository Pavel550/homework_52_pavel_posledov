from django.urls import path
from . import views
from django.views.generic import RedirectView
from webapp.views import \
    TodoCreateView,TodoDetailView,TodoListWiew, TodoDeleteView,TodoUpdateView
urlpatterns = [
    path('', TodoListWiew.as_view(), name='home'),
    path('todo/add/', TodoCreateView.as_view(), name='add_todo'),
    path('todo/<int:pk>/detail', TodoDetailView.as_view(), name='detail_todo'),
    path('todo/<int:pk>/delete', TodoDeleteView.as_view(), name = 'delete_todo'),
    path('todo/<int:pk>/update', TodoUpdateView.as_view(), name='todo_update'),

]