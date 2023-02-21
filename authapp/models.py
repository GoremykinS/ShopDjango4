from django.db import models
from django.contrib.auth.models import AbstractUser


class ShopUser(AbstractUser):
    city = models.CharField(max_length=64, verbose_name="город", blank=True)
    phone_number = models.CharField(
        max_length=14, verbose_name="номер телефона", blank=False
    )
    avatar = models.ImageField(upload_to="users_avatars", blank=True)
