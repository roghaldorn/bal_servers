from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    email = models.EmailField(blank=True, verbose_name='Email', unique=True)
    age = models.PositiveIntegerField(verbose_name='Возраст', **NULLABLE)
    avatar = models.ImageField(upload_to='users', **NULLABLE)

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
