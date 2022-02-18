from django.urls import path
from .views import FuncionariosView, FuncionarioListVeiw

urlpatterns = [
    path('', FuncionariosView.as_view(), name='funcionarios'),
    path('funcionario_list/', FuncionarioListVeiw.as_view(), name='funcionarios_list'),
]
