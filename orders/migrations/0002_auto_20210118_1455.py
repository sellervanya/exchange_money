# Generated by Django 3.1.4 on 2021-01-18 07:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='operation',
            old_name='amount',
            new_name='rate',
        ),
        migrations.AddField(
            model_name='operation',
            name='status',
            field=models.CharField(choices=[(0, 'created'), (1, 'accepted'), (2, 'declined'), (3, 'undefined')], default=0, max_length=20),
        ),
        migrations.AlterField(
            model_name='operation',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 18, 14, 55, 10, 869849), editable=False),
        ),
        migrations.AlterField(
            model_name='order',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 18, 14, 55, 10, 869849), editable=False),
        ),
    ]