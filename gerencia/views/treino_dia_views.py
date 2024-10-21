from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import Aluno, TiposTreinamento
from ..serializers import CadastrarTreinosSerializer
import datetime

class TreinoDoDiaAPIView(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request, pk, *args, **kwargs):
        try:
            # Busca o aluno pelo ID
            aluno = Aluno.objects.get(pk=pk)
            
            # Obtém o dia da semana atual
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
            
            # Mapeia o nome do dia para o formato usado no modelo
            dia_semana = dias_semana_map[dia_atual]

            # Filtra os treinos do aluno para o dia da semana atual
            treino_do_dia = aluno.tipos_treinamento.filter(dia_semana=dia_semana)

            # Serializa o treino para retornar na resposta
            treinos_serializer = CadastrarTreinosSerializer(treino_do_dia, many=True)

            # Verifica se há treinos para o dia, caso contrário, retorna uma mensagem
            if not treino_do_dia:
                return Response({"mensagem": f"Não há treinos para {dia_semana}."}, status=status.HTTP_200_OK)

            # Retorna o treino do dia
            return Response({
                "nome_aluno": aluno.nome,
                "treino_do_dia": treinos_serializer.data
            }, status=status.HTTP_200_OK)

        except Aluno.DoesNotExist:
            return Response({"erro": "Aluno não encontrado."}, status=status.HTTP_404_NOT_FOUND)
