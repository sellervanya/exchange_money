from django.db import models


TYPE_STATUS = (
    ('Buy', 'Покупка'),
    ('Sell', 'Продажа'),
)


class Order(models.Model):
    ''' Модель отвечающая за создание заявки на операцию с валютой'''
    user = models.ForeignKey(
        'users.User',
        on_delete=models.SET_NULL, null=True,
        verbose_name='Пользователь'
        )

    currency = models.ForeignKey(
        'currency.Currency',
        on_delete=models.SET_NULL, null=True,
        verbose_name='Валюта'
        )

    amount = models.PositiveIntegerField(
        verbose_name='Сумма',
        )
    created_at = models.DateTimeField(
        auto_now_add=True,
        editable=False, verbose_name='Дата заявки'
        )
    operation_type = models.CharField(
        max_length=10,
        choices=TYPE_STATUS, verbose_name='Тип операции'
        )

    def __str__(self):
        return f'''User:{self.user}|
                    Amount:{self.amount}|
                    Currency:{self.currency.short_name}|
                    DateTime:{self.created_at}'''

    class Meta():
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


OPERATION_STATUS = (
    ('created', 'Создана'),
    ('accept', 'Исполнена'),
    ('decilne', 'Отклонена'),
    ('wait', 'В ожидании'),
)


class Operation(models.Model):
    '''Модель отвечающая за хранение информации об операции'''
    order = models.OneToOneField(
        Order,
        on_delete=models.CASCADE,
        verbose_name='Заказ'
        )

    operator = models.ForeignKey(
        'users.User',
        on_delete=models.SET_NULL, null=True,
        verbose_name='Оператор'
        )

    rate = models.PositiveIntegerField(verbose_name='Курс валюты')

    update_at = models.DateTimeField(
        auto_now=True,
        editable=False,
        verbose_name='Дата обработки заявки'
        )

    status = models.CharField(
        choices=OPERATION_STATUS,
        auto_created='created', max_length=20,
        verbose_name='Статус операции'
        )

    def __str__(self):
        return f'''Operation: №{self.id}|
                Order: №{self.order.id}|
                User: {self.order.user.username}|
                Ammount: {self.order.amount}|
                {self.order.currency.name}'''

    @classmethod
    def get_by_status(cls, status_str: str):
        return cls.objects.filter(status=status_str)

    class Meta():
        verbose_name = 'Операция'
        verbose_name_plural = 'Операции'
