from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from user.models import User
from user.serializer import UserSerializer
class UserCreateView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            print(serializer.validated_data.get('phone'))
            user = User.objects.create(**serializer.validated_data)
            user.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetailView(APIView):
    def get(self, request):
        users = User.objects.filter(phone=request.query_params.get('phone'))
        serializer = UserSerializer(users[0])
        response = {
            'name': serializer.data.get('name'),
            'phone': serializer.data.get('phone'),
            'balance': users[0].balance
        }
        return Response(response, status=status.HTTP_200_OK)