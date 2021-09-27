from django.db import models
from  ad.models import Ad

class Real_Estate_Ad(Ad):
    category = 'Недвижимость'
    square = models.PositiveIntegerField('Площадь')
    location = models.CharField('Район', max_length=100)

    class Meta:
        verbose_name = 'Недвижимость'
        verbose_name_plural = 'Недвижимость'
