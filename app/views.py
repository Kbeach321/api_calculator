from django.shortcuts import render
from app.models import Operation


class OperationListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = OperationSerializer

    def get_queryset(self):
        if:
            pass
            
