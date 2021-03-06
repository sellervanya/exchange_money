# Generated by Django 3.1.4 on 2021-01-29 04:15

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20210122_1944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='document_id',
            field=models.CharField(default='', max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(default='', max_length=17, unique=True, validators=[django.core.validators.RegexValidator(message='Incorrect format phone number', regex='^\\+?1?\\d{8,12}$')]),
        ),
    ]
