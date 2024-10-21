from rest_framework import serializers
from ..models import TiposTreinamento

class CadastrarTreinosSerializer(serializers.ModelSerializer):
    class Meta:
        model = TiposTreinamento
        fields = "__all__"
