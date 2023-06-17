from django.urls import path
from . import views





urlpatterns = [
    path('', views.home,),
    path('add', views.add_new_todo,),
    path('complete/<todo_id>', views.complete_todo,),
    path('delete', views.delete_todo,),

]