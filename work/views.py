import rest_framework
from .serializers import WorkSerializer
from .models import Work
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework import status

class CreateWorkAPIView(APIView):
    def post(self,request):
        serializer = WorkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WorkListAPIView(ListAPIView):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer

class WorkUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer
    
class WorkDeleteAPIView(DestroyAPIView):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer
