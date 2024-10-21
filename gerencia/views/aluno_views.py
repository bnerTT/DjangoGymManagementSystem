from rest_framework import generics, status
from ..models import Aluno
from ..serializers import AlunoSerializer, CadastrarTreinosSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

class AlunoListCreateAPIView(generics.ListCreateAPIView):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
    # permission_classes = [IsAuthenticated]

class AlunoRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
    # permission_classes = [IsAuthenticated]

class BaterPontoAPIView(APIView):
    permission_classes = [IsAuthenticated]

    list_valores = []

    def get(self, request, pk, *args, **kwargs):
        try:
            aluno = Aluno.objects.get(pk=pk)
            dias_inicial = aluno.dias_treino_inicial
            dias_restantes_semana = aluno.dias_treino - aluno.treinos_realizados_semana.count()
            if dias_restantes_semana > 0:
                mensagem = f"Você tem {dias_restantes_semana} dias de treino restantes na semana."
                dias_restantes_semana = Aluno.objects.update(dias_treino=dias_restantes_semana-1)
            else:
                mensagem = "Você já treinou todos os dias da semana."
                dias_restantes_semana = Aluno.objects.update(dias_treino=dias_inicial)

            return Response({"mensagem": mensagem}, status=status.HTTP_200_OK)
        except Aluno.DoesNotExist:
            return Response({"erro": "Aluno não encontrado."}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request, pk, *args, **kwargs):
        try:
            aluno = Aluno.objects.get(pk=pk)

            resposta = aluno.bater_ponto()

            aluno.save()

            return Response({"mensagem": resposta}, status=status.HTTP_200_OK)
        except Aluno.DoesNotExist:
            return Response({"erro": "Aluno não encontrado."}, status=status.HTTP_404_NOT_FOUND)
        
class TreinoAlunoAPIView(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request, pk, *args, **kwargs):
        try:
            aluno = Aluno.objects.get(pk=pk)
            treinos = aluno.tipos_treinamento.all()
            treinos_serializer = CadastrarTreinosSerializer(treinos, many=True)

            return Response({
                "nome_aluno": aluno.nome,
                "treinos": treinos_serializer.data
            }, status=status.HTTP_200_OK)
            
        except Aluno.DoesNotExist:
            return Response({"erro": "Aluno não encontrado."}, status=status.HTTP_404_NOT_FOUND)
        
        
    def post(self, request, pk, *args, **kwargs):
        try:
            aluno = Aluno.objects.get(pk=pk)
            treino = request.data.get('treino')

            aluno.tipos_treinamento.add(treino)

            return Response({"mensagem": "Treino adicionado com sucesso."}, status=status.HTTP_200_OK)
        except Aluno.DoesNotExist:
            return Response({"erro": "Aluno não encontrado."}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk, *args, **kwargs):
        try:
            aluno = Aluno.objects.get(pk=pk)
            treino = request.data.get('treino')

            aluno.tipos_treinamento.remove(treino)

            return Response({"mensagem": "Treino removido com sucesso."}, status=status.HTTP_200_OK)
        except Aluno.DoesNotExist:
            return Response({"erro": "Aluno não encontrado."}, status=status.HTTP_404_NOT_FOUND)
        

