from django.db import models
from ad.models import Ad

class Other_Ad(Ad):
    '''Category other DB model'''
    category = 'Другое'

    class Meta:
        verbose_name = 'Другое'
        verbose_name_plural = 'Другое'
