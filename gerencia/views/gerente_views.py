from rest_framework.response import Response
from rest_framework.views import APIView
from ..models import Aluno, Instrutor
from ..serializers import SerializersFactory
from rest_framework.permissions import IsAuthenticated

factory = SerializersFactory()

class GerenteListAPIView(APIView):
    def get(self, request, *args, **kwargs):
        instrutores = Instrutor.objects.all()
        instrutor_serializer = factory.get_serializer('instrutor')(instrutores, many=True)

        alunos = Aluno.objects.all()
        aluno_serializer = factory.get_serializer('aluno')(alunos, many=True)

        data = {
            "instrutores": instrutor_serializer.data,
            "alunos": aluno_serializer.data,
        }

        return Response(data)
