from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import AddressSerializer
from rest_framework.exceptions import NotFound
from .models import Address

# Create your views here.
class Addresses(APIView):
    def get(self, request):
        addresses = Address.objects.all()
        serializer = AddressSerializer(addresses,many=True)
        return Response(serializer.data)
    

class AddressesDetail(APIView):
    def get_object(self, id):
        try:
            return Address.objects.get(id=id)
        except Address.DoesNotExist:
            raise NotFound
        
    def get(self, request, id):
        address = self.get_object(id)
        if address is None:
            return Response({'error':'Address not found'})
        serializer = AddressSerializer(address)
        return Response(serializer.data)
    

class CreateUserAddress(APIView):
    def post(self,request, user_id):
        # 역직렬화 (client의 jason data => object)
        serializer = AddressSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user_id=user_id)
            return Response(serializer.data)
        return Response(serializer.errors)