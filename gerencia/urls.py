from django.urls import path
from .views import (
    AlunoListCreateAPIView,
    AlunoRetrieveUpdateDestroyAPIView,
    InstrutorListCreateAPIView,
    GerenteListAPIView,
    BaterPontoAPIView,
    CadastrarTreinosAPIView,
    TreinoAlunoAPIView,
    TreinoDoDiaAPIView,
)

urlpatterns = [
    path('alunos/', AlunoListCreateAPIView.as_view(), name='aluno-list-create'), # Lista co todos os alunos
    path('alunos/<int:pk>/', AlunoRetrieveUpdateDestroyAPIView.as_view(), name='aluno-detail'), # Detalhes de um aluno
    path('alunos/<int:pk>/bater-ponto/', BaterPontoAPIView.as_view(), name='aluno-bater-ponto'), # Bater ponto de um aluno
    path('alunos/<int:pk>/treinos/', TreinoAlunoAPIView.as_view(), name='aluno-treinos'), # Treinos de um aluno
    path('alunos/<int:pk>/treino-dia/', TreinoDoDiaAPIView.as_view(), name='treino-do-dia'), # Treino do dia
    path('cadastrar-treinos/', CadastrarTreinosAPIView.as_view(), name='aluno-cadastrar'), # Cadastrar treinos
    path('instrutores/', InstrutorListCreateAPIView.as_view(), name='instrutor-list-create'), # Lista com todos os instrutores
    path('gerentes/', GerenteListAPIView.as_view(), name='gerente-list-create'), # Todos os dados do sistema para o gerente
]
