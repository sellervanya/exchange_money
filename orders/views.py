from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from . models import Operation, Order
from . forms import OrderForm


@login_required
def get_my_orders(request):
    operations = Operation.objects.filter(order__user=request.user.pk)
    return render(request, 'orders/my_orders.html', {'operations': operations})


@login_required
def get_complete_orders(request):
    operations = Operation.objects.filter(order__user=request.user.pk).filter(status='accept')
    return render(request, 'orders/complete_orders.html', {'operations': operations})


@login_required
def add_order(request):
    form = OrderForm(data=request.POST)
    if request.method == 'POST':
        if form.is_valid():
            data = form.cleaned_data
            data.update({'user': request.user})
            order = Order.objects.create(**data)
            if data['operation_type'] == 'Buy':
                rate = order.currency.rate_buy
            else:
                rate = order.currency.rate_sell
            Operation.objects.create(order=order, rate=rate, status='created')
            return redirect('get_my_orders')
    else:
        return render(request, 'orders/add_order.html', context={'form': form})
