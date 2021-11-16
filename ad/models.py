from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Ad(models.Model):
    '''Base abstract class for the DB model. Any category model must inherit from this class'''
    title = models.CharField('Заголовок', max_length=100)
    text = models.TextField('Описание')
    date = models.DateTimeField('Дата и время', auto_now_add=True)
    max_price = models.PositiveIntegerField('Максимальная цена')
    category = ''
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        abstract = True
    
    def __str__(self):
        return self.title

