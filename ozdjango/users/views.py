from django.shortcuts import render
from rest_framework.views import APIView
from .models import User
# Create your views here.

class Users(APIView):
    def get(self, request):
        users = User.objects.all()
        return users