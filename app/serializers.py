from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from app.models import Operation

class OperationSerializer(ModelSerializer):

    class Meta:
        fields = "__all__"
        read_only_fields = ["owner", "result"]
        model = Operation
