from django.contrib import admin
from ..models import TiposTreinamento

@admin.register(TiposTreinamento)
class TiposTreinoAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "nome_treino",
    ]

    search_fields = [
        "nome_treino",
    ]

    list_filter = [
        "nome_treino",
    ]