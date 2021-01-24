from django.db import models
import django.utils.timezone

TYPE_STATUS = (
    ('Покупка', 'Покупка'),
    ('Продажа', 'Продажа'),
)


class Order(models.Model):
    ''' Модель отвечающая за создание заявки на операцию с валютой'''
    user = models.ForeignKey(
        'users.User',
        on_delete=models.SET_NULL, null=True
        )

    currency = models.ForeignKey(
        'currency.Currency',
        on_delete=models.SET_NULL, null=True
        )

    amount = models.PositiveIntegerField()
    date_time = models.DateTimeField(
        default=django.utils.timezone.now,
        editable=False)

    operation_type = models.CharField(
        max_length=10,
        choices=TYPE_STATUS)

    def __str__(self):
        return f'''User:{self.user}|
                    Amount:{self.amount}|
                    Currency:{self.currency.short_name}|
                    DateTime:{self.date_time}'''

    class Meta():
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


OPERATION_STATUS = (
    ('created', 'создан'),
    ('accept', 'подтвержден'),
    ('decilne', 'отклонен'),
    ('wait', 'в ожидании'),
)


class Operation(models.Model):
    '''Модель отвечающая за хранение информации об операции'''
    order = models.OneToOneField(
        Order,
        on_delete=models.SET_NULL, null=True
        )

    operator = models.ForeignKey(
        'users.User',
        on_delete=models.SET_NULL, null=True
        )

    currency = models.ForeignKey(
        'currency.Currency',
        on_delete=models.SET_NULL, null=True
        )

    rate = models.PositiveIntegerField()

    date_time = models.DateTimeField(
        default=django.utils.timezone.now,
        editable=False)

    status = models.CharField(
        choices=OPERATION_STATUS,
        default=0, max_length=20
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

    @classmethod
    def get_by_user(cls, userid: str):
        return cls.objects.filter(order=userid)

    class Meta():
        verbose_name = 'Операция'
        verbose_name_plural = 'Операции'
