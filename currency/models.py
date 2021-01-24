from django.db import models


class Currency(models.Model):
    name = models.CharField(max_length=30, unique=True)
    short_name = models.CharField(max_length=20, unique=True)
    symbol = models.CharField(max_length=20, unique=True)
    rate_sell = models.PositiveIntegerField(default=1)
    rate_buy = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.name}|{self.short_name}|{self.symbol}'

    class Meta():
        verbose_name = 'Валюта'
        verbose_name_plural = 'Валюта'
