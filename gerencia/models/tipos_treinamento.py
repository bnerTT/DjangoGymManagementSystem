from django.db import models

class TiposTreinamento(models.Model):
    """
    A classe TiposTreinamento serve para armazenar
    os tipos de treinamento do sistema.

    Além de fazer as implementações relacionadas
    a um único objeto do tipo TiposTreinamento.
    """

    DIAS_SEMANA_CHOICES = [
        ('Segunda', 'Segunda-feira'),
        ('Terca', 'Terça-feira'),
        ('Quarta', 'Quarta-feira'),
        ('Quinta', 'Quinta-feira'),
        ('Sexta', 'Sexta-feira'),
        ('Sabado', 'Sábado'),
        ('Domingo', 'Domingo'),
    ]

    nome_treino = models.CharField(
        max_length=100,
        verbose_name="Nome do Treinamento",
        default='',
    )

    nome_exercicio = models.CharField(
        max_length=100,
        verbose_name="Nome do Exercício",
        default='',
    )

    series = models.IntegerField(
        verbose_name="Séries",
        default=0,
    )

    repeticoes = models.IntegerField(
        verbose_name="Repetições",
        default=0,
    )

    tempo_descanso = models.IntegerField(
        verbose_name="Tempo de Descanso",
        default=0,
    )

    dia_semana = models.CharField(
        max_length=10, 
        choices=DIAS_SEMANA_CHOICES, 
        verbose_name="Dia da Semana",
        default='',
    )

    def __str__(self):
        return f"{self.nome_treino} - {self.nome_exercicio} ({self.dia_semana})"

    class Meta:
        app_label = "gerencia"
        verbose_name = "Tipo de Treinamento"
        verbose_name_plural = "Tipos de Treinamento"