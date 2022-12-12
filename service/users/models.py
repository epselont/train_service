from django.contrib.auth.models import AbstractUser
from django.core.validators import (MaxLengthValidator, MinLengthValidator,
                                    RegexValidator)
from django.db import models

MAX_LENGTH = 150
MIN_LENGTH = 1
MIN_LENGTH_ERR_MSG = f'Введите не менее {MIN_LENGTH} символа(-ов).'
MAX_LENGTH_ERR_MSG = f'Введите не более {MAX_LENGTH} символа(-ов).'


class User(AbstractUser):

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = (
        'username',
        'first_name',
        'patronymic',
        'last_name',
        'position',
        'password')

    ROLES = (
        ('ADMIN', 'Администратор'),
        ('USER', 'Пользователь')
    )

    role = models.CharField(
        verbose_name="Роль",
        max_length=10,
        choices=ROLES,
        default='USER'
    )

    email = models.EmailField(
        verbose_name='Почтовый адрес',
        unique=True
    )

    username = models.CharField(
        verbose_name='Логин',
        max_length=MAX_LENGTH,
        unique=True,
        validators=[
            MinLengthValidator(
                MIN_LENGTH,
                MIN_LENGTH_ERR_MSG
            ),
            RegexValidator(
                '^[\w.@+-]+\Z',
                'Можно использовать русские или латинские символы, '
                'числа, знаки: "." и "@"'
            ),
            MaxLengthValidator(
                MAX_LENGTH,
                MAX_LENGTH_ERR_MSG
            )
        ]
    )

# TODO продумать валидацию для ФИО(с заглавной и тд)
    first_name = models.CharField(
        verbose_name='Имя пользователя',
        max_length=MAX_LENGTH,
        validators=[
            MinLengthValidator(
                MIN_LENGTH,
                MIN_LENGTH_ERR_MSG
            )
        ]
    )

    patronymic = models.CharField(
        verbose_name='Отчество пользователя',
        max_length=MAX_LENGTH,
        validators=[
            MIN_LENGTH,
            MIN_LENGTH_ERR_MSG
        ]
    )
    last_name = models.CharField(
        verbose_name='Фамилия Пользователя',
        max_length=MAX_LENGTH,
        validators=[
            MinLengthValidator(
                MIN_LENGTH,
                MIN_LENGTH_ERR_MSG
            )
        ]
    )

    position = models.CharField(
        verbose_name='Должность',
        max_length=MAX_LENGTH,
        validators=[
            MinLengthValidator(
                MIN_LENGTH,
                MIN_LENGTH_ERR_MSG
            )
        ]
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('username',)

    @property
    def is_admin(self):
        return self.role == 'ADMIN'

    @property
    def is_user(self):
        return self.role == 'USER'

    def __str__(self):
        return f'{self.last_name} {self.first_name[:0]}.{self.patronymic[:0]}.'
