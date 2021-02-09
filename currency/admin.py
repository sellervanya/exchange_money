from django.contrib import admin

from .models import Currency


class CustomCurrencyAdmin(admin.ModelAdmin):
    model = Currency
    list_display = (
        'id', 'name', 'short_name',
        'symbol', 'rate_sell', 'rate_buy',
        )

    list_display_links = ('id',)
    ordering = ('pk',)


admin.site.register(Currency, CustomCurrencyAdmin)
