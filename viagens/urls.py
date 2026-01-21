from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    # Servidores
    path("viajantes/", views.lista_viajantes, name="lista_viajantes"),
    path("cadastro/viajante/", views.cadastro_viajante, name="cadastro_viajante"),
    path("viajantes/editar/<int:viajante_id>/", views.editar_viajante, name="editar_viajante"),
    path("viajantes/excluir/<int:viajante_id>/", views.excluir_viajante, name="excluir_viajante"),
    # veiculos
    path("veiculos/", views.lista_veiculos, name="lista_veiculos"),
    path("veiculos/cadastro/", views.cadastro_veiculo, name="cadastro_veiculo"),
    path("veiculos/editar/<int:veiculo_id>/", views.editar_veiculo, name="editar_veiculo"),
    path("veiculos/excluir/<int:veiculo_id>/", views.excluir_veiculo, name="excluir_veiculo"),
]

