import pytest
from . import models


def test_credit(db):
    data = {
        'first_name': 'Максим',
        'last_name': 'Балабанов',
        'iin': '911106451061',
        'phone': '77778464774'
    }
    person = models.Person.objects.create(**data)
    data = {
        'cash': 30,
        'status': 'active',
        'person': person
    }
    credit = models.Credit.objects.create(**data)
    assert isinstance(credit, models.Credit)
