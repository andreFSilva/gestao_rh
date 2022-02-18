from django.urls import path
from .views import DocumentosView


urlpatterns = [
    path('', DocumentosView.as_view(), name='documentos'),
]