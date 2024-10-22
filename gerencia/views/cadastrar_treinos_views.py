from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from ..models import TiposTreinamento
from ..serializers import SerializersFactory

factory = SerializersFactory()

class CadastrarTreinosAPIView(APIView):
    def get(self, request, *args, **kwargs):
        nome_treino = request.GET.get('nome_treino')
        nome_exercicio = request.GET.get('nome_exercicio')
        series = request.GET.get('series')
        repeticoes = request.GET.get('repeticoes')
        tempo_descanso = request.GET.get('tempo_descanso')

        if not all([nome_treino, nome_exercicio, series, repeticoes, tempo_descanso]):
            return Response({"erro": "Todos os campos são obrigatórios."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            novo_treino = TiposTreinamento.objects.create(
                nome_treino=nome_treino,
                nome_exercicio=nome_exercicio,
                series=int(series),
                repeticoes=int(repeticoes),
                tempo_descanso=int(tempo_descanso)
            )

            treino_serializer = factory.get_serializer('tipos_treinamento')(novo_treino)

            return Response({
                "mensagem": "Treino cadastrado com sucesso.",
                "treino": treino_serializer.data
            }, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"erro": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request, *args, **kwargs):
        dados = request.data
        if not all([dados.get('nome_treino'), dados.get('nome_exercicio'), dados.get('series'), dados.get('repeticoes'), dados.get('tempo_descanso')]):
            return Response({"erro": "Todos os campos são obrigatórios."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            novo_treino = TiposTreinamento.objects.create(
                nome_treino=dados['nome_treino'],
                nome_exercicio=dados['nome_exercicio'],
                series=int(dados['series']),
                repeticoes=int(dados['repeticoes']),
                tempo_descanso=int(dados['tempo_descanso'])
            )

            treino_serializer = factory.get_serializer('tipos_treinamento')(novo_treino)

            return Response({
                "mensagem": "Treino cadastrado com sucesso.",
                "treino": treino_serializer.data
            }, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"erro": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
