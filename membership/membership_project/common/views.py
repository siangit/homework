from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from .models import Feed

class AddressDetail(APIView):
	def get_object(self, feed_id):