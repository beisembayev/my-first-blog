from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=25, verbose_name="Имя")
    last_name = models.CharField(max_length=25, verbose_name="Фамилия")
    iin = models.CharField(max_length=12, verbose_name="ИИН")
    phone = models.CharField(max_length=11, verbose_name="Телефон")


class Credit(models.Model):
    CHOICES = (
        ('CREATED', 'created'),
        ('ACTIVE', 'active'),
        ('PAID', 'paid'),
    )
    status = models.CharField(max_length=150, verbose_name="статус", choices=CHOICES)
    cash = models.DecimalField(max_digits=5, decimal_places=3, verbose_name="Денги")
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
