from django.shortcuts import render, get_object_or_404
from . models import Currency


def currency_rate(request):
    rates = Currency.objects.filter(pk__gt=1)
    return render(request, 'rate.html', context={'rates': rates})
