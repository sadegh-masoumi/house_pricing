from django.db import models
from app_user.models import User


class Address(models.Model):
    """
    address model
    """
    name = models.CharField(max_length=32, unique=True)

    def __str__(self):
        """to string"""
        return self.name


class Apartment(models.Model):
    """
    apartment model
    """
    area = models.PositiveIntegerField()
    room = models.PositiveSmallIntegerField()
    has_parking = models.BooleanField(default=False)
    has_warehouse = models.BooleanField(default=False)
    has_elevator = models.BooleanField(default=False)
    address = models.ForeignKey(Address, models.CASCADE)
    price = models.FloatField()
    person = models.ForeignKey(User, models.CASCADE)

    def __str__(self):
        """to string"""
        return self.address
