from django.contrib.auth.decorators import login_required
from django.shortcuts import (redirect, render)

from .forms import TodoAddForm
from .models import Task


# home
@login_required
def home(request):
    if request.method == 'POST':
        form = TodoAddForm(request.POST)
        if form.is_valid():
            usr = form.save(commit=False)
            usr.user_id = request.user.id
            usr.save()
            return redirect('home')
    else:
        form = TodoAddForm()
    tasks = Task.objects.filter(user_id=request.user.id).order_by('-created_on')
    done = Task.objects.filter(user_id=request.user.id, is_complete=True)
    undone = Task.objects.filter(user_id=request.user.id, is_complete=False)
    context = {'form': form, 'tasks': tasks, 'done': done, 'undone': undone}
    return render(request, 'bud/index.html', context)


# delete
def delete(request, pk):
    item = Task.objects.get(id=pk)
    if request.method == 'POST':
        if item.is_complete is False:
            item.is_complete = True
            item.save()
        return redirect('home')
    return render(request, 'bud/index.html')


# profile
@login_required
def profile(request, username):
    if request.user.is_authenticated:
        return render(request, 'profile/profile_details.html')
    else:
        return redirect('home')
