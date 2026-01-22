from django.urls import path
from . import views

urlpatterns = [
    path("ajax/servidores/", views.buscar_servidores, name="buscar_servidores"),
    path("ajax/motoristas/", views.buscar_motoristas, name="buscar_motoristas"),
    # dashboard
    path("", views.dashboard, name="dashboard"),
    # oficios
    path("oficios/", views.lista_oficios, name="lista_oficios"),
    path("oficios/cadastro/", views.cadastro_oficio, name="cadastro_oficio"),
    path("oficios/editar/<int:oficio_id>/", views.editar_oficio, name="editar_oficio"),
    path("oficios/excluir/<int:oficio_id>/", views.excluir_oficio, name="excluir_oficio"),
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

