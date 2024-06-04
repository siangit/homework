from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import AddressSerializer
from .models import Address

# Create your views here.
class Addresses(APIView):
    def get(self, request):
        addresses = Address.objects.all()
        serializer = AddressSerializer(addresses,many=True)
        return Response(serializer.data)