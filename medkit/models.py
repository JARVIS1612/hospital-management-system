from django.db import models
from authentication.models import Users

# Create your models here.
class Orders(models.Model):
    username = models.ForeignKey(Users, on_delete=models.CASCADE)
    prescription = models.ImageField(blank=False, null=False, upload_to='images/')
    datetime = models.DateTimeField(auto_now_add=True)
    is_ready = models.BooleanField(default=False)
    is_taken = models.BooleanField(default=False)
    taken_at = models.DateTimeField(blank=True, null=True)
    uniquecode = models.IntegerField(blank=True, null=True)
    cost = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=True)