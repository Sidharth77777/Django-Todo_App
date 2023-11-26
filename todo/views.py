from django.shortcuts import render
from django.http.response import HttpResponse,HttpResponseRedirect
from django.shortcuts import get_object_or_404

from todo.models import Todos
from todo.forms import TodosForm

# Create your views here.

def index(request):
    if request.user.is_authenticated:
        todos = Todos.objects.filter(todo_user=request.user,is_completed=False,is_deleted=False)
        completed = Todos.objects.filter(todo_user=request.user,is_completed=True,is_deleted=False)
        form = TodosForm(request.POST)
    
        context = {
            'todo' : todos,
            'completed' : completed,
            'form' : form,
        }
    else:
        context = {}    
    return render (request, 'todo.html', context=context)


def create_task(request):
    if request.user.is_authenticated:
        todos = Todos.objects.filter(todo_user=request.user,is_completed=False)
        completed = Todos.objects.filter(todo_user=request.user,is_completed=True)
        form = TodosForm(request.POST)
        
        todo = request.POST.get('todo')
        if todo != None:
            todos.create(
                todo_user=request.user,
                todo = todo,
                is_completed = False,
                is_deleted = False,
                is_reverted = False
            )
            todo = TodosForm()
        context = {
            'todo' : todos,
            'completed' : completed,
            'form' : form,
        }
        return HttpResponseRedirect('/')
        
    else:
        context = {
            'message' : 'Login to create a task!!!'
        }
        return render (request, 'todo.html', context=context)


def delete_task(request,id):
    if request.user.is_authenticated:
        instance = Todos.objects.filter(todo_user=request.user,id=id)
        if instance:
            instance.is_deleted=True
            instance.delete()
        
    return HttpResponseRedirect('/')    


def delete_tasks(request):
    if request.user.is_authenticated:
        todo = Todos.objects.filter(todo_user=request.user,is_deleted=False,is_completed=True)
        if todo:
            todo.delete()
    
    return HttpResponseRedirect('/')


def complete_task(request,id):
    if request.user.is_authenticated:
        instance = get_object_or_404(Todos,id=id)
        if instance:
            instance.is_completed = True
            instance.save()
        
    return HttpResponseRedirect('/')    


def revert_task(request,id):
    if request.user.is_authenticated:
        instance = get_object_or_404(Todos,id=id)
        if instance:
            instance.is_completed = False
            instance.save()
    
    return HttpResponseRedirect('/')


def edit_task(request,id):
    if request.user.is_authenticated:
        instance = get_object_or_404(Todos,id=id)
        value = instance.todo
        
    context = {
        'value' : value,
        'instance' : instance,
    }
    return render(request,'edit.html',context=context)


def submit_edit_task(request,id):
    if request.user.is_authenticated:
        instance = get_object_or_404(Todos,id=id)
        edited_task = request.POST.get('edited')
        if instance:
            instance.todo = edited_task
            instance.save()
    
    return HttpResponseRedirect('/')