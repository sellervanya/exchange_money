from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


class User(AbstractUser):
    GEN_CHOICES = [
        ('Мужчина', 'Мужчина'),
        ('Женщина', 'Женщина'),
        ]

    first_name = models.CharField(max_length=20, blank=False,
                                  null=False, default='')
    last_name = models.CharField(max_length=20, blank=False,
                                 null=False, default='')
    phone_regex = RegexValidator(regex=r'^\+?1?\d{8,12}$',
                                 message="Incorrect format phone number")
    phone_number = models.CharField(validators=[phone_regex], max_length=17,
                                    blank=False, default='')
    document_id = models.CharField(max_length=20, default='')
    gender = models.CharField(choices=GEN_CHOICES, max_length=10, blank=False,
                              null=False, default='m')

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        db_table = 'auth_user'
