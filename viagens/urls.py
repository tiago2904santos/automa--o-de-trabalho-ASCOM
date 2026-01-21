from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("cadastro/viajante/", views.cadastro_viajante, name="cadastro_viajante"),
]
