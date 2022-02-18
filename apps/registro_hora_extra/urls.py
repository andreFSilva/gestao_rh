from django.urls import path
from .views import RegistroHoraExtraView


urlpatterns = [
    path('', RegistroHoraExtraView.as_view(), name='hora_extra'),
]