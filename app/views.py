from django.shortcuts import render
from app.models import Operation
from app.serializers import OperationSerializer
from rest_framework import generics
from app.permissions import IsOwnerOrReadOnly


class OperationListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = OperationSerializer

    def get_queryset(self):
            return Operation.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):

        data = serializer.validated_data

        operator = data['operator']
        operand_one = int(data['operand_one'])
        operand_two = int(data['operand_two'])

        result = 0
        if operator == "+":
            result = operand_one + operand_two
        elif operator == "-":
            result = operand_one - operand_two
        elif operator == "*":
            result = operand_one * operand_two
        elif operator == "/":
            result = operand_one / operand_two

        serializer.save(owner= self.request.user, result = result)

class OperationRetrieveDestroyAPIView(generics.RetrieveDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Operation.objects.all()
    serializer_class = OperationSerializer
