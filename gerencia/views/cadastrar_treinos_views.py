from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from ..models import TiposTreinamento

class CadastrarTreinosAPIView(APIView):
    def get(self, request, *args, **kwargs):
        # Obter os parâmetros da URL
        nome_treino = request.GET.get('nome_treino')
        nome_exercicio = request.GET.get('nome_exercicio')
        series = request.GET.get('series')
        repeticoes = request.GET.get('repeticoes')
        tempo_descanso = request.GET.get('tempo_descanso')

        # Verificar se todos os parâmetros estão presentes
        if not all([nome_treino, nome_exercicio, series, repeticoes, tempo_descanso]):
            return Response({"erro": "Todos os campos são obrigatórios."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Criar um novo tipo de treinamento com os dados obtidos
            novo_treino = TiposTreinamento.objects.create(
                nome_treino=nome_treino,
                nome_exercicio=nome_exercicio,
                series=int(series),
                repeticoes=int(repeticoes),
                tempo_descanso=int(tempo_descanso)
            )

            # Retornar a resposta com o novo objeto criado
            return Response({
                "mensagem": "Treino cadastrado com sucesso.",
                "treino": {
                    "nome_treino": novo_treino.nome_treino,
                    "nome_exercicio": novo_treino.nome_exercicio,
                    "series": novo_treino.series,
                    "repeticoes": novo_treino.repeticoes,
                    "tempo_descanso": novo_treino.tempo_descanso
                }
            }, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({"erro": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def post(self, request, *args, **kwargs):
        # Obter os dados do corpo da requisição
        dados = request.data

        # Verificar se todos os campos estão presentes
        if not all([dados.get('nome_treino'), dados.get('nome_exercicio'), dados.get('series'), dados.get('repeticoes'), dados.get('tempo_descanso')]):
            return Response({"erro": "Todos os campos são obrigatórios."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Criar um novo tipo de treinamento com os dados obtidos
            novo_treino = TiposTreinamento.objects.create(
                nome_treino=dados['nome_treino'],
                nome_exercicio=dados['nome_exercicio'],
                series=int(dados['series']),
                repeticoes=int(dados['repeticoes']),
                tempo_descanso=int(dados['tempo_descanso'])
            )

            # Retornar a resposta com o novo objeto criado
            return Response({
                "mensagem": "Treino cadastrado com sucesso.",
                "treino": {
                    "nome_treino": novo_treino.nome_treino,
                    "nome_exercicio": novo_treino.nome_exercicio,
                    "series": novo_treino.series,
                    "repeticoes": novo_treino.repeticoes,
                    "tempo_descanso": novo_treino.tempo_descanso
                }
            }, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({"erro": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
