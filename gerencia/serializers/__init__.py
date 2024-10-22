from .aluno_serializers import AlunoSerializer
from .instrutor_serializers import InstrutorSerializer
from .cadastrar_treinos_serializers import CadastrarTreinosSerializer
from .serializers_factory import SerializersFactory

__all__ = [
    AlunoSerializer,
    InstrutorSerializer,
    CadastrarTreinosSerializer,
    SerializersFactory,
]
