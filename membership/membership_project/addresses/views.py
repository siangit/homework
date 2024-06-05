from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import AddressSerializer
from rest_framework.exceptions import NotFound
from .models import Address

# Create your views here.

########### APIView => 데이터 교환을 위한 class#########

class Addresses(APIView):
#Function-Based Views(FBV) 방식 (단일함수로 작성된 로직)
# 장점: 간결하고 직관적/////또 다른 방식(Class-Based View(CBV))
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
        #request.data = user로 부터 받은 데이터
        serializer = AddressSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user_id=user_id)
            return Response(serializer.data)
        return Response(serializer.errors)

class UpdateUserAddress(APIView):
##########데이터 불러와서 읽기##########
    def get_object(self, pk):
        try:
            return Address.objects.get(pk=pk)
        except Address.DoesNotExist:
            raise NotFound
        
    def put(self, request, pk):
        address = self.get_object(pk)
        if address is None:
            return Response(({'error'}))
        
##########update save 코드########
        serializer = AddressSerializer(address, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
class DeleteUserAddress(APIView):
    def get_object(self,pk):
        try:
            return Address.objects.get(pk=pk)
        except Address.DoesNotExist:
            raise NotFound
    
    def delete(self, request, pk):
        address = self.get_object(pk)
        if address is None:
            return Response(({'error'}))