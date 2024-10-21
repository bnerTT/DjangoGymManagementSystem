from rest_framework import generics
from ..models import Instrutor
from ..serializers import InstrutorSerializer
from rest_framework.permissions import IsAuthenticated


class InstrutorListCreateAPIView(generics.ListCreateAPIView):
    queryset = Instrutor.objects.all()
    serializer_class = InstrutorSerializer
    # permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()