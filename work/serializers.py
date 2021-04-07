import rest_framework

from rest_framework.serializers import ModelSerializer
from .models import Work

class WorkSerializer(ModelSerializer):
    class Meta:
        model = Work
        fields = "__all__"