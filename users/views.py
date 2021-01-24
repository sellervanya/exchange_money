from django.shortcuts import redirect, render, get_object_or_404
from django.http import Http404
from django.contrib.auth import logout


def user_settings(request):
    if request.user.is_authenticated:
        return render(request, "profile.html")
    else:
        raise Http404('Your\'e is not authorized user')


def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('index')
