from django.db import models
from app_user.models import User


class Address(models.Model):
    name = models.CharField(max_length=32, unique=True)


class Apartment(models.Model):
    area = models.PositiveIntegerField()
    room = models.PositiveSmallIntegerField()
    has_parking = models.BooleanField()
    has_warehouse = models.BooleanField()
    has_elevator = models.BooleanField()
    address = models.ForeignKey(Address, models.CASCADE)
    price = models.FloatField()
    person = models.ForeignKey(User, models.CASCADE)
