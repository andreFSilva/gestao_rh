from django.db import models


class Departamento(models.Model):
    nome = models.CharField(max_length=150, help_text='Nome do departamento')

    class Meta:
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'
        ordering = ['nome']

    def __str__(self):
        return self.nome
