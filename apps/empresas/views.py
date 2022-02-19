from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Empresa


class EmpresasView(LoginRequiredMixin, TemplateView):
    template_name = 'empresas/empresas.html'


class EmpresasListView(ListView):
    model = Empresa
    template_name = 'empresas/empresas_list.html'

    def get_context_data(self, **kwargs):
        context = super(EmpresasListView, self).get_context_data(**kwargs)
        context['empresas'] = Empresa.objects.order_by('id').all()
        return context

