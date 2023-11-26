from django.contrib import admin
from todo.models import Todos

# Register your models here.

class TodosAdmin(admin.ModelAdmin):
    list_display = ['id','todo','todo_user','is_completed']
    
admin.site.register(Todos, TodosAdmin)