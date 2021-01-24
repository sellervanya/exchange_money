from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from . models import Operation


def get_my_orders(request):
    try:
        if (request.user.groups.get(id=3)):
            operations = Operation.get_by_status('crt')
            return render(request, 'orders.html', {'operations': operations})
    except ObjectDoesNotExist:
        return redirect('index')
