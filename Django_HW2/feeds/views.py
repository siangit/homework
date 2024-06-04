from django.shortcuts import render
from rest_framework.views import APIView
from .models import Feed
from .serializers import FeedSerializer
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
# Create your views here.

class Feeds(APIView):
    def get(self, request):
        feeds = Feed.objects.all()

        #object -> JSON (serlialize)
        serializer = FeedSerializer(feeds, many=True)

        return Response(serializer.data)
    
    # 역직렬화 (client가 보내준 json -> object)
    def post(self,request):
        serializer = FeedSerializer(data=request.data)
        if serializer.is_valid():
            # feed = serializer.save(user=request.user)

            # serializer = FeedSerializer(feed)
            print("post serializer", serializer)

            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
        

class FeedDetail(APIView):
    def get_object(self, feed_id):
        try:
            return Feed.objects.get(id=feed_id)
        except Feed.DoesNotExist:
            raise NotFound
    
    def get(self, request, feed_id):
        feed = self.get_object(feed_id)
        # feed (obejct) => json => serializer

        serializer = FeedSerializer(feed)
        print(serializer)

        return Response(serializer.data)