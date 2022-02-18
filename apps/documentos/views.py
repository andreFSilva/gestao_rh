from django.shortcuts import render
from django.views.generic import TemplateView


class DocumentosView(TemplateView):
    template_name = 'documentos/documentos.html'
