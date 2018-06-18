from django.shortcuts import render
from app.models import Operation
from app.serializers import OperationSerializer
from rest_framework import generics
from django.db.models import Q
from app.permissions import IsOwnerOrReadOnly


class OperationListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = OperationSerializer

    def get_queryset(self):
            return Operation.objects.filter(Q(owner=self.request.user))

    def perform_create(self, serializer):
        if operator == "+":
            return result == operand_one + operand_two
        elif operator == "-":
            return result == operand_one - operand_two
        elif operator == "*":
            return result == operand_one * operand_two
        elif operator == "/":
            return result == operand_one / operand_two

        serializer.save(result= self.request.result)

class OperationRetrieveDestroyAPIView(generics.RetrieveDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Operation.objects.all()
    serializer_class = OperationSerializer
