from django.shortcuts import render
from django.views.generic import TemplateView
from ..funcionarios.models import Funcionario


class HomeView(TemplateView):
    template_name = 'pages/index.html'
    model = Funcionario

    '''def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['usuarios'] = Funcionario.objects.all()
        return context'''

    def get_context_data(self, **kwargs):
        f = Funcionario.objects.all()
        usuario = f.last()
        context = super(HomeView, self).get_context_data(**kwargs)
        context['usuarios'] = usuario

        return context
