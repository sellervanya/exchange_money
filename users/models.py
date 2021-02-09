from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


GEN_CHOICES = [
    ('Man', 'Мужчина'),
    ('Woman', 'Женщина'),
    ]


class User(AbstractUser):
    ''' Клас переописывает стандартный клас пользователя'''

    name_regex = RegexValidator(
        regex=r'^[a-zA-Zа-яА-Я]{2,20}$',
        message="Некорректное значение, используете буквы А-я, A-z"
        )

    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{8,12}$',
        message="Некорректный номер телефона"
        )

    first_name = models.CharField(
        verbose_name='Имя',
        max_length=20, blank=False,
        null=False, validators=[name_regex]
        )

    last_name = models.CharField(
        verbose_name='Фамилия',
        max_length=20, blank=False,
        null=False, validators=[name_regex]
        )

    phone_number = models.CharField(
        verbose_name='Номер телефона',
        unique=True, validators=[phone_regex],
        max_length=12, blank=False
        )

    document_id = models.CharField(
        verbose_name='Номер документа',
        unique=True, max_length=20
        )

    gender = models.CharField(
        verbose_name='Пол',
        choices=GEN_CHOICES, max_length=10, blank=False,
        null=False, default='Мужчина'
        )

    email = models.EmailField(
        unique=True, blank=False, null=False,
        )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        db_table = 'auth_user'
