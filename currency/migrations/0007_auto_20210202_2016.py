# Generated by Django 3.1.4 on 2021-02-02 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0006_auto_20210124_1925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currency',
            name='rate_buy',
            field=models.FloatField(default=1, verbose_name='Курс покупки'),
        ),
        migrations.AlterField(
            model_name='currency',
            name='rate_sell',
            field=models.FloatField(default=1, verbose_name='Курс продажи'),
        ),
    ]