from django.shortcuts import (redirect, render)
from django.http import (HttpResponse, HttpRequest)
from .models import Todo


# home
def home(request):
    content = Todo.objects.all()
    context = {'tasks': content}
    return render(request, 'index.html', context)


# insert
def insert(request: HttpRequest):
    todo = Todo(content=request.POST['content'])
    todo.save()
    return redirect('/')


# delete
def delete(request, todo_id):
    delete_task = Todo.objects.get(id=todo_id)
    delete_task.delete()
    return redirect('/')
