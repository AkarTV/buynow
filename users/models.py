from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model

from phonenumber_field.modelfields import PhoneNumberField

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = PhoneNumberField(blank = True, verbose_name = 'Номер телефона')
    avatar = models.ImageField(blank = True, upload_to='avatars', verbose_name='Фото профиля')

