from django.shortcuts import render, redirect
from .forms import CreateUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
# Create your views here.
def registration_page(request):
    if request.user.is_authenticated:
        return redirect('')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'User has been successefly registered, Please Log In!')
                return redirect('accounts:login')
        else:
            CreateUserForm()
        context = {
            'form': form
        }
        return render(request, 'accounts/register.html', context)

def login_page(request):
    if request.user.is_authenticated:
        return redirect('')
    else:
        if request.method == 'POST':
            form = AuthenticationForm(request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('')
            else:
                messages.error(request, 'Invalid Username or Password!')
        form = AuthenticationForm()
        context = {
            'form': form
        }
        return render(request, 'accounts/login.html', context)


def logout_page(request):
    logout(request)
    return redirect('accounts:login')
