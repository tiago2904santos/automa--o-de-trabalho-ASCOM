from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("cadastro/viajante/", views.cadastro_viajante, name="cadastro_viajante"),
    path("viajantes/", views.lista_viajantes, name="lista_viajantes"),
    path("cadastro/veiculo/", views.cadastro_veiculo, name="cadastro_veiculo"),
    path("veiculos/", views.lista_veiculos, name="lista_veiculos")
]
