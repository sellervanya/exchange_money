# Generated by Django 3.1.4 on 2021-01-18 09:58

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='document_id',
            field=models.CharField(default='020', max_length=20),
        ),
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('m', 'Мужчина'), ('f', 'Женщина')], default='m', max_length=10),
        ),
        migrations.AddField(
            model_name='user',
            name='phone_number',
            field=models.CharField(default='79999999', max_length=17, validators=[django.core.validators.RegexValidator(message='Incorrect format phone number', regex='^\\+?1?\\d{9,10}$')]),
        ),
    ]
