from django.core.validators import MinValueValidator
from django.db import models


class Item(models.Model):
    name = models.CharField(
        verbose_name='Наименование товара',
        max_length=200)
    description = models.TextField(
        verbose_name='Описание',
        blank=True,
        null=True)
    price = models.FloatField(
        verbose_name='Стоимость',
        validators=[MinValueValidator(0.1)])

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return f'{self.name} | {self.price}'
