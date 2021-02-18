from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required

from . models import Operation, Order
from . forms import OrderForm, OperationForm


@login_required
def get_my_orders(request):
    operations = Operation.objects.filter(order__user=request.user.pk)
    return render(request, 'orders/my_orders.html', {'operations': operations})


@login_required
def get_complete_orders(request):
    operations = Operation.objects.filter(order__user=request.user.pk).filter(status='accept')
    return render(request, 'orders/complete_orders.html', {'operations': operations})


@permission_required('orders.add_order')
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


@permission_required('orders.change_operation')
@login_required
def get_new_operations(request):
    operations = Operation.objects.filter(operator=None)
    return render(request, 'orders/new_operations.html', {'operations': operations})


@permission_required('orders.change_operation')
@login_required
def get_operation_by_id(request, id):
    operation = get_object_or_404(Operation.objects.filter(id=id).filter(operator=None))
    form = OperationForm(initial={'status': operation.status})
    if request.method == 'POST':
        form = OperationForm(request.POST, instance=operation)
        if form.is_valid():
            if operation.order.operation_type == 'Buy':
                operation.rate = operation.order.currency.rate_buy
            else:
                operation.rate = operation.order.currency.rate_sell
            operation.operator = request.user
            form.save()
            return redirect('get_new_operations')
    return render(request, 'orders/operation.html', {'operation': operation, 'form': form})
