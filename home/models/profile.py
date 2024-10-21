from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    """
    A classe Profile serve para armazernar
    os(as) profiles do sistema.

    Além de fazer as implementações relacionadas
    a um único objeto do tipo Profile.
    """

    usuario = models.OneToOneField(
        User,
        verbose_name="Usuário",
        on_delete=models.CASCADE,
    )

    CHOICE_TIPO_USUARIO = (
        ("Aluno", "Aluno"),
        ("Profesor", "Professor"),
        ("Gerente", "Gerente"),
    )

    tipo_usuario = models.CharField(
        max_length=100,
        choices=CHOICE_TIPO_USUARIO,
        verbose_name="Tipo de Usuário",
        default="",
    )

    def __str__(self):
        return f"{self.usuario}"

    class Meta:
        app_label = "home"
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"
