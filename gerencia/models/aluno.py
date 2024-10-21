from django.db import models
from .tipos_treinamento import TiposTreinamento

class Aluno(models.Model):
    """
    A classe Aluno serve para armazenar
    os(as) alunos(as) do sistema.

    Além de fazer as implementações relacionadas
    a um único objeto do tipo Aluno.
    """

    nome = models.CharField(
        max_length=100,
        verbose_name="Nome",
    )

    cpf = models.CharField(
        max_length=14,
        verbose_name="CPF",
    )

    telefone = models.CharField(
        max_length=15,
        verbose_name="Telefone",
    )

    email = models.EmailField(
        verbose_name="Email",
    )

    data_nascimento = models.DateField(
        verbose_name="Data de Nascimento",
    )

    dias_treino = models.IntegerField(
        verbose_name="Dias de Treino restantes",
        default=0,
    )

    dias_treino_inicial = models.IntegerField(
        verbose_name="Dias de Treino Inicial",
        default=0,
    )

    tipos_treinamento = models.ManyToManyField(
        TiposTreinamento,
        verbose_name="Tipos de Treinamento",
        related_name="tipos_treinamento",
        blank=True,
    )

    treinos_realizados_semana = models.ManyToManyField(
        TiposTreinamento,
        verbose_name="Treinos Realizados na Semana",
        related_name="treinos_realizados",
        blank=True,
    )

    def bater_ponto(self):
        dias_restantes_semana = self.dias_treino - self.treinos_realizados_semana.count()
        if dias_restantes_semana > 0:
            return f"Você tem {dias_restantes_semana} dias de treino restantes na semana."
        elif dias_restantes_semana == 0:
            self.dias_treino = 3
            return "Você já treinou todos os dias da semana."

    def __str__(self):
        return f"{self.nome}"

    class Meta:
        app_label = "gerencia"
        verbose_name = "Aluno"
        verbose_name_plural = "Alunos"