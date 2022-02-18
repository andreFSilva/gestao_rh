from django.shortcuts import render
from django.views.generic import TemplateView


class DepartamentosView(TemplateView):
    template_name = 'departamentos/departamentos.html'


