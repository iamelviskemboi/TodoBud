from django.shortcuts import (redirect, render)
from django.http import (HttpResponse, HttpRequest)
from .models import Todo


# home
def home(request):
    content = Todo.objects.all()
    context = {content: 'content'}
    return render(request, 'index.html', context)


# insert
def insert(request:HttpRequest):
    todo = Todo(content = request.POST['content'])
    todo.save()
    return redirect('/')
