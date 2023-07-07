from django.urls import path
from . import views
from django.views.generic import RedirectView
from views import TodoCreateView,TodoDetailView,TodoListWiew
urlpatterns = [
    path('', TodoListWiew.as_view(), name='home'),
    path('todo/add/', TodoCreateView.as_view(), name='add_todo'),
    path('todo/<int:pk>/', TodoDetailView.as_view(), name='detail_todo'),
    path('todo/<int:pk>/delete', views.delete_todo_, name = 'delete_todo'),
    path('todo/<int:pk>/update', views.todo_update, name='todo_update'),

]