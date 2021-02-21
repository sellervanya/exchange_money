from django.shortcuts import redirect, render
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required

from .forms import SignUpForm, SignInForm, UserForm


@login_required
def user_settings(request):
    msg = ''
    user = request.user
    form = UserForm(instance=user, initial={'password': None})
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            password = form.cleaned_data['password']
            if authenticate(username=user.username, password=password):
                form.save()
                msg = f'Вы обновили информацию профиля'
            else:
                msg = 'Введите верный пароль'
    return render(request, "users/profile.html", context={'form': form, 'msg': msg})


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
