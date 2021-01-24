# Generated by Django 3.1.4 on 2021-01-18 09:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20210118_1455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operation',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime.now, editable=False),
        ),
        migrations.AlterField(
            model_name='operation',
            name='status',
            field=models.CharField(choices=[('crt', 'created'), ('accpt', 'accepted'), ('declnd', 'declined'), ('undf', 'undefined')], default=0, max_length=20),
        ),
        migrations.AlterField(
            model_name='order',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 18, 16, 51, 2, 573742), editable=False),
        ),
    ]
