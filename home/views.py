import rest_framework
from .serializers import HomeSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from home.models import Home
from rest_framework import status
from rest_framework.generics import ListAPIView,RetrieveUpdateAPIView, DestroyAPIView



class CreateHomeAPIView(APIView):

    def post(self, request, format=None):
        serializer = HomeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class HomeListAPIView(ListAPIView):
    queryset = Home.objects.all()
    serializer_class = HomeSerializer

class HomeUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Home.objects.all()
    serializer_class = HomeSerializer
    
class HomeDeleteAPIView(DestroyAPIView):
    queryset = Home.objects.all()
    serializer_class = HomeSerializer