from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name= 'home'),
    path('todo/add/', views.add_new_todo, name = 'add_todo'),
    path('todo/<int:pk>/', views.detail_todo, name = 'detail_todo'),
    path('todo/delete/', views.delete_todo, name = 'delete_todo'),

]