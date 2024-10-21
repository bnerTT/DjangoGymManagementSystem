from rest_framework.response import Response
from rest_framework.views import APIView
from ..models import Aluno, Instrutor
from ..serializers import AlunoSerializer, InstrutorSerializer
from rest_framework.permissions import IsAuthenticated

class GerenteListAPIView(APIView):
    # permission_classes = [IsAuthenticated]
    def get(self, request, *args, **kwargs):
        instrutores = Instrutor.objects.all()
        instrutor_serializer = InstrutorSerializer(instrutores, many=True)

        alunos = Aluno.objects.all()
        aluno_serializer = AlunoSerializer(alunos, many=True)

        data = {
            "instrutores": instrutor_serializer.data,
            "alunos": aluno_serializer.data,
        }

        return Response(data)
