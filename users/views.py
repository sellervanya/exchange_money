from django.shortcuts import redirect, render
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required

from .forms import SignUpForm, SignInForm


@login_required
def user_settings(request):
    return render(request, "users/profile.html")


@login_required
def user_logout(request):
    logout(request)
    return redirect('index')


def signup(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            my_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=my_password)
            login(request, user)
            return redirect('index')
    return render(request, 'users/signup.html', {'form': form})


def signin(request):
    form = SignInForm()
    if request.method == 'POST':
        form = SignInForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            my_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=my_password)
            login(request, user)
            return redirect('index')
    return render(request, 'users/signin.html', {'form': form})
