from rest_framework import generics
from ..models import Instrutor
from ..serializers import SerializersFactory
from rest_framework.permissions import IsAuthenticated

factory = SerializersFactory()

class InstrutorListCreateAPIView(generics.ListCreateAPIView):
    queryset = Instrutor.objects.all()
    serializer_class = factory.get_serializer('instrutor')

    def perform_create(self, serializer):
        serializer.save()
