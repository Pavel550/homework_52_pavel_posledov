from django.urls import path
from . import views


urlpatterns = [
    path('', views.home,),
    path('/add', views.add_new_todo,),
    path('todo/', views.detail_todo,),
    path('delete', views.delete_todo,),

]