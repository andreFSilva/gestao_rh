from django.shortcuts import render
from django.views.generic import TemplateView


class RegistroHoraExtraView(TemplateView):
    template_name = 'registrohoraextra/registro_hora_extra.html'
