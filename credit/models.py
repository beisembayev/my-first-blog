from django.db import models
from django.utils.timezone import now


class Person(models.Model):
    First_name = models.CharField(max_length=25, verbose_name="Имя")
    Last_name = models.CharField(max_length=25, verbose_name="Фамилия")
    iin = models.CharField(max_length=12, verbose_name="ИИН")
    Phone = models.CharField(max_length=11, verbose_name="Телефон")


class CreditStatus(models.Model):
    CHOICES = (
        ('CREATED', 'created'),
        ('ACTIVE', 'active'),
        ('PAID', 'paid'),
    )
    status = models.CharField(max_length=150, verbose_name="статус", choices=CHOICES)
    credit = models.ForeignKey(Person, related_name='statuses', on_delete=models.CASCADE)




# Create your models here.
