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

