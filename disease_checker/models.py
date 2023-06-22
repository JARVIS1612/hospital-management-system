from django.db import models


# Create your models here.
class Diseases(models.Model):
    disease = models.CharField(max_length=50, primary_key=True)


class Departments(models.Model):
    Departments = models.CharField(max_length=100, primary_key=True)