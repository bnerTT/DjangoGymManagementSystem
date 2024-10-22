from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import Aluno
from ..serializers import SerializersFactory
import datetime

factory = SerializersFactory()

class TreinoDoDiaAPIView(APIView):
    def get(self, request, pk, *args, **kwargs):
        try:
            aluno = Aluno.objects.get(pk=pk)
            dia_atual = datetime.datetime.now().strftime('%A')
            dias_semana_map = {
                'Monday': 'Segunda',
                'Tuesday': 'Terca',
                'Wednesday': 'Quarta',
                'Thursday': 'Quinta',
                'Friday': 'Sexta',
                'Saturday': 'Sabado',
                'Sunday': 'Domingo'
            }
            dia_semana = dias_semana_map[dia_atual]
            treino_do_dia = aluno.tipos_treinamento.filter(dia_semana=dia_semana)
            treinos_serializer = factory.get_serializer('cadastrar_treinos')(treino_do_dia, many=True)

            if not treino_do_dia:
                return Response({"mensagem": f"Não há treinos para {dia_semana}."}, status=status.HTTP_200_OK)

            return Response({
                "nome_aluno": aluno.nome,
                "treino_do_dia": treinos_serializer.data
            }, status=status.HTTP_200_OK)
        except Aluno.DoesNotExist:
            return Response({"erro": "Aluno não encontrado."}, status=status.HTTP_404_NOT_FOUND)
