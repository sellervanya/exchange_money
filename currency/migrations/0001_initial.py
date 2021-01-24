# Generated by Django 3.1.4 on 2021-01-18 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
                ('short_name', models.CharField(max_length=20, unique=True)),
                ('symbol', models.CharField(max_length=20, unique=True)),
            ],
            options={
                'verbose_name': 'Валюта',
                'verbose_name_plural': 'Валюта',
            },
        ),
    ]