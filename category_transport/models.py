from django.db import models
from  ad.models import Ad

class Transport_Ad(Ad):
    category = 'Транспорт'
    brand = models.CharField('Марка', max_length=40)
    model = models.CharField('Модель', max_length=60)
    year = models.PositiveIntegerField('Год')

    class Meta:
        verbose_name = 'Транспорт'
        verbose_name_plural = 'Транспорт'
