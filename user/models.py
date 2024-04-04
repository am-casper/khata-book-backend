from django.db import models

class User(models.Model):
    name=models.CharField(max_length=100)
    phone=models.CharField(max_length=10, primary_key=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    