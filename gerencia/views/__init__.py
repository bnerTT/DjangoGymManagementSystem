from .aluno_views import (
    AlunoListCreateAPIView,
    AlunoRetrieveUpdateDestroyAPIView,
    BaterPontoAPIView,
    TreinoAlunoAPIView
)
from .instrutor_views import InstrutorListCreateAPIView
from .gerente_views import GerenteListAPIView
from .cadastrar_treinos_views import CadastrarTreinosAPIView
from .treino_dia_views import TreinoDoDiaAPIView

__all__ = [
    AlunoListCreateAPIView,
    AlunoRetrieveUpdateDestroyAPIView,    
    BaterPontoAPIView,
    CadastrarTreinosAPIView,
    GerenteListAPIView,
    InstrutorListCreateAPIView,
    TreinoAlunoAPIView,
    TreinoDoDiaAPIView,
]
