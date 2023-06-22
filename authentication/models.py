from django.db import models
from django.contrib.auth.models import AbstractUser
from disease_checker.models import Departments


blood_groups = [('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('O+', 'O+'), ('O-', 'O-'), ('AB+', 'AB+'),
                ('AB-', 'AB-')]
genders = [('Male', 'Male'), ('Female', 'Female'), ('N/A', 'Not want to declare')]


# Create your models here.
class Users(AbstractUser):
    id = None
    username = models.CharField(max_length=50, blank=False, primary_key=True)
    first_name = models.CharField(max_length=20, blank=False, null=True)
    last_name = models.CharField(max_length=20, blank=False, null=True)
    email = models.CharField(max_length=30, blank=False, null=True, unique=True)
    number = models.PositiveIntegerField(blank=False, null=True, unique=True)
    age = models.PositiveIntegerField(null=True, blank=False)
    gender = models.CharField(max_length=10, choices=genders, default='Male')
    blood_group = models.CharField(max_length=3, choices=blood_groups, default='A+')
    date_time = models.DateTimeField(auto_now_add=True)
    is_patient = models.BooleanField(default=True)
    is_doctor = models.BooleanField(default=False)
    is_pharma = models.BooleanField(default=False)


class Doctors(models.Model):
    id = None
    username = models.ForeignKey(Users, primary_key=True, on_delete=models.CASCADE)
    department = models.ForeignKey(Departments, null=True, blank=True, on_delete=models.CASCADE)

class Pharma(models.Model):
    id = None
    username = models.ForeignKey(Users, primary_key=True, on_delete=models.CASCADE)
