# Generated by Django 3.1.4 on 2021-02-02 13:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0007_auto_20210202_2016'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='operation',
            name='amount',
        ),
        migrations.RemoveField(
            model_name='operation',
            name='currency',
        ),
        migrations.RemoveField(
            model_name='operation',
            name='date_time',
        ),
        migrations.RemoveField(
            model_name='order',
            name='date_time',
        ),
        migrations.AddField(
            model_name='operation',
            name='rate',
            field=models.PositiveIntegerField(default=1, verbose_name='Курс валюты'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='operation',
            name='status',
            field=models.CharField(auto_created='created', choices=[('created', 'Создана'), ('accept', 'Исполнена'), ('decilne', 'Отклонена'), ('wait', 'В ожидании')], default=1, max_length=20, verbose_name='Статус операции'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='operation',
            name='update_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата обработки заявки'),
        ),
        migrations.AddField(
            model_name='order',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Дата заявки'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='operation_type',
            field=models.CharField(choices=[('Buy', 'Покупка'), ('Sell', 'Продажа')], default=1, max_length=10, verbose_name='Тип операции'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='operation',
            name='operator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Оператор'),
        ),
        migrations.AlterField(
            model_name='operation',
            name='order',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='orders.order', verbose_name='Заказ'),
        ),
        migrations.AlterField(
            model_name='order',
            name='amount',
            field=models.PositiveIntegerField(verbose_name='Сумма'),
        ),
        migrations.AlterField(
            model_name='order',
            name='currency',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='currency.currency', verbose_name='Валюта'),
        ),
        migrations.AlterField(
            model_name='order',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
    ]
