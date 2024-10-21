from django.db import models
from .aluno import Aluno

class Instrutor(models.Model):
    """
    A classe Instrutor serve para armazenar
    os(as) instrutores(as) do sistema.

    Além de fazer as implementações relacionadas
    a um único objeto do tipo Instrutor.
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

    alunos_responsavel = models.ManyToManyField(
        Aluno,
        verbose_name="Alunos Responsável",
        related_name="alunos_responsavel",
        blank=True,
    )

    def __str__(self):
        return f"{self.nome}"

    class Meta:
        app_label = "gerencia"
        verbose_name = "Instrutor"
        verbose_name_plural = "Instrutores"