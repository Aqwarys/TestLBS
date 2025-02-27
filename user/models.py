import random

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

# Create your models here.


# class User(AbstractUser):
#     username = models.CharField(unique=False, max_length=50)

def generate_card_number():
    """Генерирует случайный 16-значный номер карты"""
    return "".join(str(random.randint(0, 9)) for _ in range(16))

from datetime import timedelta, datetime

def generate_expiration_date():
    expirtion_date = datetime.now() + timedelta(days=5*365)
    return expirtion_date.date()

def generate_cvv():
    return random.randint(100,999)

class BankAccount(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.PositiveIntegerField(default=0)
    card_number = models.CharField(max_length=16, unique=True, blank=True)
    expiration_date = models.DateField(blank=True)
    cvv = models.CharField(max_length=3, blank=True)
    created_at = models.DateField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.card_number:
            self.card_number = generate_card_number()
        if not self.cvv:
            self.cvv = generate_cvv()
        if not self.expiration_date:
            self.expiration_date = generate_expiration_date()
        super().save(*args, **kwargs)