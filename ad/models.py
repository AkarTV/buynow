from django.db import models

class Ad(models.Model):
    title = models.CharField('Заголовок', max_length=100)
    text = models.TextField('Описание')
    date = models.DateTimeField('Дата и время', auto_now_add=True)
    max_price = models.PositiveIntegerField('Максимальная цена')
    category = ''

    class Meta:
        abstract = True
    
    def __str__(self):
        return self.title


class Transport_Ad(Ad):
    category = 'Транспорт'
    brand = models.CharField('Марка', max_length=40)
    model = models.CharField('Модель', max_length=60)
    year = models.PositiveIntegerField('Год')

    class Meta:
        verbose_name = 'Транспорт'
        verbose_name_plural = 'Транспорт'


class Real_Estate_Ad(Ad):
    category = 'Недвижимость'
    square = models.PositiveIntegerField('Площадь')
    location = models.CharField('Район', max_length=100)

    class Meta:
        verbose_name = 'Недвижимость'
        verbose_name_plural = 'Недвижимость'


class Other_Ad(Ad):
    category = 'Другое'

    class Meta:
        verbose_name = 'Другое'
        verbose_name_plural = 'Другое'

