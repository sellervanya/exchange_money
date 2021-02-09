from django.db import models


class Currency(models.Model):
    '''Модель отвечающая за хранение данных о валюте'''
    name = models.CharField(
        max_length=30, unique=True,
        verbose_name='Наименование'
        )

    short_name = models.CharField(
        max_length=20, unique=True,
        verbose_name='Короткое наименование'
        )

    symbol = models.CharField(
        max_length=20, unique=True,
        verbose_name='Символ'
        )

    rate_sell = models.FloatField(
        default=1, verbose_name='Курс продажи'
        )

    rate_buy = models.FloatField(
        default=1, verbose_name='Курс покупки')

    def __str__(self):
        return f'{self.name}|{self.short_name}|{self.symbol}'

    class Meta():
        verbose_name = 'Валюта'
        verbose_name_plural = 'Валюта'
