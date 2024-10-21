from django.contrib import admin
from ..models import Instrutor

@admin.register(Instrutor)
class InstrutorAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "nome",
    ]

    search_fields = [
        "nome",
    ]

    list_filter = [
        "nome",
    ]

    filter_horizontal = [
        'alunos_responsavel',
    ]