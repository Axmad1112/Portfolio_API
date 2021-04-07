from rest_framework.serializers import ModelSerializer
from .models import Home

class HomeSerializer(ModelSerializer):
    class Meta:
        model = Home
        fields = '__all__'