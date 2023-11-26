from django.urls import path
from todo.views import index,create_task,delete_tasks,delete_task,complete_task,revert_task,edit_task,submit_edit_task

app_name = 'todo'

urlpatterns = [
    path('', index, name='index'),
    path('create/', create_task, name='createTask'),
    path('deleteAll/', delete_tasks, name='deleteTasks'),
    path('delete/<int:id>/', delete_task, name='deleteTask'),
    path('complete/<int:id>/', complete_task, name='completeTask'),
    path('revert/<int:id>/', revert_task, name='revertTask'),
    path('edit/<int:id>/', edit_task, name='editTask'),
    path('edited/<int:id>', submit_edit_task, name='editedTask'),
    
]