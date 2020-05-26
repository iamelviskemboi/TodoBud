from django.shortcuts import (redirect, render)
from django.contrib.auth import (authenticate, login, logout)
from django.contrib.auth.views import login_required
from django.contrib import messages

from .models import (Profile)
from .forms import (RegistrationForm)


# ACCOUNTS -> SIGN IN
def sign_in(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.warning(request, 'Incorrect Username or Password!')
    else:
        return redirect('home')
    return render(request, 'accounts/login.html')


# ACCOUNTS -> SIGN OUT
@login_required
def sign_out(request):
    logout(request)
    return redirect('login')


# ACCOUNTS -> REGISTER
def register(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = RegistrationForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data['username']
                password = form.cleaned_data['password2']
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('home')
        else:
            form = RegistrationForm()
        context = {'form': form}
        return render(request, 'accounts/register.html', context)
    else:
        return redirect('home')


# ACCOUNTS -> SETTINGS
@login_required
def settings(request, username):
    return render(request, 'accounts/settings.html')
