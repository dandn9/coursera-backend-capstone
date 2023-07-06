from django.db import models
from datetime import date
from django.utils import timezone


# Create your models here.
class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    inventory = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.title} : {str(self.price)}"


class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField()
    bookingDate = models.DateField(default=timezone.now)
