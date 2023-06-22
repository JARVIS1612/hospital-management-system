from django.db import models
from authentication.models import Users, Doctors
from disease_checker.models import Departments

class TimeSlots(models.Model):
    time_slot = models.CharField(max_length=50, primary_key=True)

class Bookings(models.Model):
    username = models.ForeignKey(Users, on_delete=models.DO_NOTHING)
    department = models.ForeignKey(Departments, on_delete=models.DO_NOTHING)
    date = models.DateField()
    time_slot = models.ForeignKey(TimeSlots, on_delete=models.DO_NOTHING)
    notes = models.TextField(max_length=500, blank=True, null=True)
    date_time = models.DateTimeField(auto_now_add=True)
    assigned_doctor = models.ForeignKey(Doctors, blank=True, null=True, related_name="assigned_doctor", on_delete=models.DO_NOTHING)
    assigned_timeslot = models.ForeignKey(TimeSlots, blank=True, null=True, related_name="assigned_timeslot", on_delete=models.DO_NOTHING)
    is_approved = models.BooleanField(default=False)
    is_checked = models.BooleanField(default=False)
    unique_code = models.IntegerField(blank=True, null=True)