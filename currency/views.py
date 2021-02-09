from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse

from . models import Currency


def currency_rate(request):
    rates = Currency.objects.all()
    return render(request, 'rate.html', context={'rates': rates})


def get_rate_by_id(request, id):
    res = get_object_or_404(Currency.objects.values('rate_buy', 'rate_sell').filter(id=id))
    return JsonResponse(res)
