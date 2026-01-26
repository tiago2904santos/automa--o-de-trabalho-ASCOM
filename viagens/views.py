from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .forms import ViajanteForm, VeiculoForm, OficioForm
from .models import Viajante, Veiculo, Oficio, Cidade
import django.db.models as models

# ================= DASHBOARD ================= #

def dashboard(request):
    return render(request, "viagens/dashboard.html")


# ==================================================== #
# ================= SERVIDORES ======================= #
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
    viajantes = Viajante.objects.all()

    q = request.GET.get("q", "")
    cargo = request.GET.get("cargo", "")
    order = request.GET.get("order", "nome")

    # 🔍 Busca
    if q:
        viajantes = viajantes.filter(
            models.Q(nome__icontains=q) |
            models.Q(cpf__icontains=q) |
            models.Q(rg__icontains=q) |
            models.Q(telefone__icontains=q)
        )

    # 🎯 Filtro cargo
    if cargo:
        viajantes = viajantes.filter(cargo=cargo)

    # ↕️ Ordenação segura
    campos_validos = ["nome", "cpf", "cargo", "telefone"]
    campo_order = order.lstrip("-")

    if campo_order in campos_validos:
        viajantes = viajantes.order_by(order)

    return render(request, "viagens/viajantes/lista_viajantes.html", {
        "viajantes": viajantes,
        "cargo_choices": Viajante._meta.get_field("cargo").choices,
        "cargo_selecionado": cargo,
        "q": q,
        "order": order,
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
# =================== VEÍCULOS ======================= #
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
    veiculos = Veiculo.objects.all()

    q = request.GET.get("q", "")
    combustivel = request.GET.get("combustivel", "")
    order = request.GET.get("order", "modelo")

    # 🔍 Busca
    if q:
        veiculos = veiculos.filter(
            models.Q(placa__icontains=q) |
            models.Q(modelo__icontains=q)
        )

    # 🎯 Filtro combustível
    if combustivel:
        veiculos = veiculos.filter(combustivel=combustivel)

    # ↕️ Ordenação segura
    campos_validos = ["modelo", "placa", "combustivel"]
    campo_order = order.lstrip("-")
    if campo_order in campos_validos:
        veiculos = veiculos.order_by(order)

    return render(request, "viagens/veiculos/lista_veiculos.html", {
        "veiculos": veiculos,
        "combustivel_choices": Veiculo._meta.get_field("combustivel").choices,
        "combustivel_selecionado": combustivel,
        "q": q,
        "order": order,
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


# ==================================================== #
# ==================== OFÍCIOS ======================= #
# ==================================================== #

def cadastro_oficio(request):
    if request.method == "POST":
        form = OficioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("cadastro_oficio")
    else:
        form = OficioForm()

    return render(request, "viagens/oficios/cadastro_oficio.html", {
        "form": form
    })


def lista_oficios(request):
    oficios = Oficio.objects.all().order_by("-oficio")

    busca = request.GET.get("q", "")
    status = request.GET.get("status", "")
    order = request.GET.get("order", "-oficio")

    # 🔍 Busca
    if busca:
        oficios = oficios.filter(
            models.Q(oficio__icontains=busca) |
            models.Q(protocolo__icontains=busca) |
            models.Q(cidade_destino__cidade__icontains=busca) |
            models.Q(estado_destino__icontains=busca) |
            models.Q(servidor__nome__icontains=busca)
        )

    # 🎯 Filtro status
    if status:
        oficios = oficios.filter(status=status)

    # ↕️ Ordenação segura
    campos_validos = ["oficio", "protocolo", "cidade_destino__cidade", "servidor__nome"]
    campo_order = order.lstrip("-")
    if campo_order in campos_validos:
        oficios = oficios.order_by(order)

    return render(request, "viagens/oficios/lista_oficios.html", {
        "oficios": oficios,
        "status_choices": Oficio._meta.get_field("status").choices,
        "status_selecionado": status,
        "q": busca,
        "order": order
    })


def editar_oficio(request, oficio_id):
    oficio = get_object_or_404(Oficio, id=oficio_id)

    if request.method == "POST":
        form = OficioForm(request.POST, instance=oficio)
        if form.is_valid():
            form.save()
            return redirect("lista_oficios")
    else:
        form = OficioForm(instance=oficio)

    return render(
        request,
        "viagens/oficios/editar_oficio.html",
        {"form": form, "oficio": oficio}
    )


def excluir_oficio(request, oficio_id):
    oficio = get_object_or_404(Oficio, id=oficio_id)

    if request.method == "POST":
        oficio.delete()
        return redirect("lista_oficios")

    return render(
        request,
        "viagens/oficios/excluir_oficio.html",
        {"oficio": oficio}
    )


def documento_oficio(request, oficio_id):
    oficio = get_object_or_404(Oficio, id=oficio_id)
    motorista_exibicao = (
        oficio.motorista.nome
        if oficio.motorista
        else oficio.motorista_nome
    )

    return render(
        request,
        "viagens/oficios/documento_oficio.html",
        {
            "oficio": oficio,
            "motorista_exibicao": motorista_exibicao,
        }
    )


# ==================================================== #
# ================ AUTOCOMPLETE AJAX ================= #
# ==================================================== #

def buscar_servidores(request):
    q = request.GET.get("q", "")
    servidores = Viajante.objects.filter(
        nome__icontains=q
    ).values("id", "nome").order_by("nome")[:7]

    data = list(servidores)
    return JsonResponse(data, safe=False)


def buscar_motoristas(request):
    q = request.GET.get("q", "")
    motoristas = Viajante.objects.filter(
        nome__icontains=q
    ).values("id", "nome").order_by("nome")[:7]

    data = list(motoristas)
    return JsonResponse(data, safe=False)


def buscar_veiculos(request):
    q = request.GET.get("q", "")
    placa = Veiculo.objects.filter(
        placa__icontains=q
    ).values("id", "placa").order_by("placa")[:7]

    data = list(placa)
    return JsonResponse(data, safe=False)

def buscar_cidades(request):
    q = request.GET.get("q", "")
    estado = request.GET.get("estado", "")

    cidades = Cidade.objects.all()

    if estado:
        cidades = cidades.filter(estado=estado)

    if q:
        cidades = cidades.filter(cidade__icontains=q)

    data = list(
        cidades.order_by("cidade")
        .values("id", "cidade")[:7]
    )

    return JsonResponse(data, safe=False)


def detalhes_viajante(request, viajante_id):
    viajante = get_object_or_404(Viajante, id=viajante_id)
    data = {
        "nome": viajante.nome,
        "rg": viajante.rg,
        "cpf": viajante.cpf,
        "cargo": viajante.cargo,
    }
    return JsonResponse(data)


def detalhes_veiculo(request, veiculo_id):
    veiculo = get_object_or_404(Veiculo, id=veiculo_id)
    data = {
        "placa": veiculo.placa,
        "modelo": veiculo.modelo,
        "combustivel": veiculo.get_combustivel_display(),
    }
    return JsonResponse(data)
