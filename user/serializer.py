from rest_framework import serializers
from phonenumber_field.serializerfields import PhoneNumberField

from user.models import User

class UserSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    phone = serializers.CharField(max_length=10)
    balance = serializers.DecimalField(max_digits=10, decimal_places=2, default=0)
    
    class Meta:
        model=User
        fields="__all__"