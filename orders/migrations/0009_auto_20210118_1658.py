# Generated by Django 3.1.4 on 2021-01-18 09:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_auto_20210118_1655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 18, 16, 58, 38, 613864), editable=False),
        ),
    ]