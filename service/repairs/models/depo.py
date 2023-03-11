from django.db import models
from django.core.validators import RegexValidator


class Depo(models.Model):
    name = models.CharField(
        verbose_name='Название депо',
        max_length=50,
        validators=[
            RegexValidator(
                r'^([а-яА-я])$',
                'Название депо должно быть только на русском.'
            )
        ]
    )
    prefix = models.CharField(
        verbose_name='Префикс',
        max_length=2,
        validators=[
            RegexValidator(
                r'[А-Я]{2}',
                'Префикс должен состоять из 2-х заглавных букв.'
            )
        ]
    )

    class Meta:
        verbose_name = 'Депо'
        ordering = ('name',)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.name = self.name.capitalize()
        super().save(*args, **kwargs)
