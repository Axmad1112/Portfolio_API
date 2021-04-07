import rest_framework
from .serializers import AboutSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import About
from rest_framework import status
from rest_framework.generics import ListAPIView,RetrieveUpdateAPIView, DestroyAPIView



class CreateAboutAPIView(APIView):

    def post(self, request, format=None):
        serializer = AboutSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AboutListAPIView(ListAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer

class AboutUpdateAPIView(RetrieveUpdateAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer
    
class AboutDeleteAPIView(DestroyAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer