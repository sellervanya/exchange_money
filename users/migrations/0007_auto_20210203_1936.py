# Generated by Django 3.1.4 on 2021-02-03 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20210202_2016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('Man', 'Мужчина'), ('Woman', 'Женщина')], default='Мужчина', max_length=10, verbose_name='Пол'),
        ),
    ]
