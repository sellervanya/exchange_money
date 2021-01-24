# Generated by Django 3.1.4 on 2021-01-22 09:03

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210118_1658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='document_id',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(default='', max_length=17, validators=[django.core.validators.RegexValidator(message='Incorrect format phone number', regex='^\\+?1?\\d{8,12}$')]),
        ),
    ]