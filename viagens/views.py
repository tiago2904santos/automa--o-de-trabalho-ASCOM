from django.shortcuts import render, redirect, get_object_or_404
from .forms import ViajanteForm, VeiculoForm
from .models import Viajante, Veiculo

# dashboard:

def dashboard(request):
    return render(request, "viagens/dashboard.html")

# ==================================================== #
# ==================SERVIDORES======================== #
# ==================================================== #


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

def editar_viajante(request, viajante_id):
    viajante = get_object_or_404(Viajante, id=viajante_id)
    if request.method == "POST":
        form = ViajanteForm(request.POST, instance=viajante)
        if form.is_valid():
            form.save()
            return redirect("lista_viajantes")
    else:
        form = ViajanteForm(instance=viajante)
    return render(
        request,
        "viagens/viajantes/editar_viajante.html",
        {"form": form, "viajante": viajante}
    )

def excluir_viajante(request, viajante_id):
    viajante = get_object_or_404(Viajante, id=viajante_id)

    if request.method == "POST":
        viajante.delete()
        return redirect("lista_viajantes")

    return render(
        request,
        "viagens/viajantes/excluir_viajante.html",
        {"viajante": viajante}
    )


# ==================================================== #
# ====================VEICULOS======================== #
# ==================================================== #


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

def editar_veiculo(request, veiculo_id):
    veiculo = get_object_or_404(Veiculo, id=veiculo_id)

    if request.method == "POST":
        form = VeiculoForm(request.POST, instance=veiculo)
        if form.is_valid():
            form.save()
            return redirect("lista_veiculos")
    else:
        form = VeiculoForm(instance=veiculo)

    return render(
        request,
        "viagens/veiculos/editar_veiculo.html",
        {"form": form, "veiculo": veiculo}
    )

def excluir_veiculo(request, veiculo_id):
    veiculo = get_object_or_404(Veiculo, id=veiculo_id)

    if request.method == "POST":
        veiculo.delete()
        return redirect("lista_veiculos")

    return render(
        request,
        "viagens/veiculos/excluir_veiculo.html",
        {"veiculo": veiculo}
    )
