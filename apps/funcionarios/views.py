from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Funcionario


class FuncionariosView(TemplateView):
    template_name = 'funcionarios/funcionarios.html'


class FuncionarioListVeiw(ListView):
    template_name = 'funcionarios/funcionario_list.html'
    model = Funcionario

    def get_context_data(self, **kwargs):
        context = super(FuncionarioListVeiw, self).get_context_data(**kwargs)
        context['funcionarios'] = Funcionario.objects.order_by('nome').all()
        return context
