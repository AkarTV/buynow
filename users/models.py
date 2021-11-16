from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

class User(AbstractUser):
    phone_number = PhoneNumberField(blank = True, null = True, verbose_name = 'Номер телефона')
    avatar = models.ImageField(blank = True, null = True, upload_to='avatars', verbose_name='Фото профиля')