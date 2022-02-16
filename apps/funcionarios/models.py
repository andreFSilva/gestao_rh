from django.db import models
from django.conf import settings
from ..departamentos.models import Departamento
from ..empresas.models import Empresa


class Funcionario(models.Model):
    """
    Funcionário
    """
    nome = models.CharField(max_length=150, help_text='Nome do funcionário')
    user = models.OneToOneField(to=settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    departamentos = models.ManyToManyField(Departamento)
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Funcionário'
        verbose_name_plural = "Funcionários"

    def __str__(self):
        return self.nome


