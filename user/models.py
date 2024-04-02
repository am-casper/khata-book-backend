from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class User(models.Model):
    name=models.CharField(max_length=100)
    phone=models.CharField(max_length=10, primary_key=True)
    