# Generated by Django 3.1.4 on 2021-02-02 13:16

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20210129_1115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='document_id',
            field=models.CharField(default='', max_length=20, unique=True, verbose_name='Номер документа'),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=20, validators=[django.core.validators.RegexValidator(message='Некорректное значение, используете буквы А-я, A-z', regex='^[a-zA-Zа-яА-Я]{2,20}$')], verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('Мужчина', 'Мужчина'), ('Женщина', 'Женщина')], default='Мужчина', max_length=10, verbose_name='Пол'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(max_length=20, validators=[django.core.validators.RegexValidator(message='Некорректное значение, используете буквы А-я, A-z', regex='^[a-zA-Zа-яА-Я]{2,20}$')], verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(default='', max_length=12, unique=True, validators=[django.core.validators.RegexValidator(message='Некорректный номер телефона', regex='^\\+?1?\\d{8,12}$')], verbose_name='Номер телефона'),
        ),
    ]