from django.shortcuts import render
from rest_framework.views import APIView
from .models import Address
from .serializers import AddressSerializer
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
# Create your views here.

class Addresses(APIView):
    def get(self, request):
        addresses = Address.objects.all()

        #object -> JSON (serlialize)
        serializer = AddressSerializer(addresses, many=True)

        return Response(serializer.data)

class AddressesDetail(APIView):
    def get_object(self, address_id):
        try:
            return Address.objects.get(id=address_id)
        except Address.DoesNotExist:
            raise NotFound
    
    def get(self, request, address_id):
        address = self.get_object(address_id)
        # address (obejct) => json => serializer

        serializer = AddressSerializer(Address)
        print(serializer)

        return Response(serializer.data)
