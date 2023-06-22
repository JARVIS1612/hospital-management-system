from django.contrib import admin
from .models import TimeSlots, Bookings
# Register your models here.

admin.site.register(TimeSlots)
admin.site.register(Bookings)