from django.urls import path
from . import views


urlpatterns = [
    path('', views.home,),
    path('todo/add/', views.add_new_todo,),
    path('todo/', views.detail_todo,),
    path('todo/delete/', views.delete_todo,),

]