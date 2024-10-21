from django.contrib import admin
from ..models import Aluno

@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "nome",
    ]

    search_fields = [
        "nome",
        "cpf",
    ]

    list_filter = [
        "nome",
        "cpf",
    ]

    filter_horizontal = [
        'tipos_treinamento',
        'treinos_realizados_semana',
    ]