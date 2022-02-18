from django.urls import path
from .views import EmpresasView, EmpresasListView


urlpatterns = [
    path('', EmpresasView.as_view(), name='empresas'),
    path('empresas_list/', EmpresasListView.as_view(), name='empresas_list'),
]