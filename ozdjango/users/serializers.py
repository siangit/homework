from rest_framework.serializers import ModelSerializer
from .models import User

class FeedUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "email")

class AddressUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "street")