from django.shortcuts import render, redirect
from .forms import ViajanteForm

def cadastro_viajante(request):
    if request.method == "POST":
        form = ViajanteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("cadastro_viajante")
    else:
        form = ViajanteForm()

    return render(request, "viagens/cadastro_viajante.html", {
        "form": form
    })

def index(request):
    return render(request, "viagens/index.html")