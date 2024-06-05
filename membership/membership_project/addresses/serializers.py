from rest_framework.serializers import ModelSerializer
from .models import Address

class AddressSerializer(ModelSerializer):
    class Meta:
        model = Address
        fields= "__all__"
        depth = 1

class AddressListSerializer(ModelSerializer):
    class Meta:
        model = Address
        fields = ["user", "street", "city", "state", "postal_code","country"]
        depth = 1