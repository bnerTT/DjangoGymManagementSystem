from rest_framework import serializers
from .aluno_serializers import AlunoSerializer
from .instrutor_serializers import InstrutorSerializer
from .cadastrar_treinos_serializers import CadastrarTreinosSerializer

class SerializersFactory:
    def __init__(self):
        # Mapeamento de nomes para classes de serializer
        self.serializers = {
            'aluno': AlunoSerializer,
            'instrutor': InstrutorSerializer,
            'tipos_treinamento': CadastrarTreinosSerializer,
            'cadastrar_treinos': CadastrarTreinosSerializer,
        }

    def get_serializer(self, model_name):
        # Retorna a classe de serializer com base no nome do modelo
        serializer_class = self.serializers.get(model_name)
        if not serializer_class:
            raise ValueError(f"Serializer para o modelo {model_name} não encontrado.")
        return serializer_class
