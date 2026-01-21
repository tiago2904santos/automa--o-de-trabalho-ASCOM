from django.shortcuts import render, redirect
from .forms import ViajanteForm, VeiculoForm
from .models import Viajante, Veiculo



def dashboard(request):
    return render(request, "viagens/dashboard.html")

def cadastro_viajante(request):
    if request.method == "POST":
        form = ViajanteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("cadastro_viajante")
    else:
        form = ViajanteForm()

    return render(request, "viagens/viajantes/cadastro_viajante.html", {
        "form": form
    })


def lista_viajantes(request):
    viajantes = Viajante.objects.all().order_by("nome")
    return render(request, "viagens/viajantes/lista_viajantes.html", {
        "viajantes": viajantes
    })


def cadastro_veiculo(request):
    if request.method == "POST":
        form = VeiculoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("cadastro_veiculo")
    else:
        form = VeiculoForm()

    return render(
        request,
        "viagens/veiculos/cadastro_veiculo.html",
        {"form": form}
    )

def lista_veiculos(request):
    veiculos = Veiculo.objects.all().order_by("modelo")
    return render(request, "viagens/veiculos/lista_veiculos.html", {
        "veiculos": veiculos
    })