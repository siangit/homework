from rest_framework.serializers import ModelSerializer
from .models import Address
from users.serializers import AddressUserSerializer

class AddressSerializer(ModelSerializer):

    Address = AddressUserSerializer()
    class Meta:
        model = Address
        fields = "__all__"

        depth = 1