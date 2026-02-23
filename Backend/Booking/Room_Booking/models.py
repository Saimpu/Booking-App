from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings   
# Create your models here.
from django.db import models

class Booking(models.Model):

    ROOM_TYPES = [
        ('suite', 'Suites'),
        ('standard', 'Standard Rooms'),
        ('deluxe', 'Deluxe Room'),
    ]

    CURRENCY_TYPES = [
        ('USD', 'US Dollar'),
        ('EUR', 'Euro'),
        ('INR','Indian')
    ]

    name = models.CharField(max_length=100, default='', blank=True)

    types = models.CharField(
        max_length=20,
        choices=ROOM_TYPES
    )

    pricepernight = models.IntegerField(default=150)

    currency = models.CharField(
        max_length=10,default='USD',
        choices=CURRENCY_TYPES
        
    )

    maxOccupency = models.IntegerField(default=1)

    description = models.TextField(max_length=1000)

    def __str__(self):
        return f"{self.name} {self.types}"

class RoomImages(models.Model):
    image=models.ImageField(upload_to="room/")
    caption=models.CharField(max_length=100,blank=True,null=True)
    room = models.ForeignKey(
        Booking,
        related_name="images",
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"Images for {self.room.name} - {self.caption or 'No caption'}"

class OccupiedDate(models.Model):
    room=models.ForeignKey(Booking,on_delete=models.CASCADE,related_name="occupiedDate")
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="booke_dates")
    date=models.DateField()
    def __str__(self):
        return f"{self.date}-{self.room.name} Booked by {self.user.username}"


class User(AbstractUser):
    email=models.EmailField(unique=True)
    full_name=models.CharField(max_length=100,default=" ")