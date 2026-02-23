from django.contrib import admin
from .models import Booking,RoomImages,OccupiedDate,User
# Register your models here.
admin.site.register(Booking)
admin.site.register(RoomImages)
admin.site.register(OccupiedDate)
# admin.site.register(User)