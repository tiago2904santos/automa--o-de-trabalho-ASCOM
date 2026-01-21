from django import forms
from .models import Viajante, Veiculo

class ViajanteForm(forms.ModelForm):
    class Meta:
        model = Viajante
        fields = ["nome", "cpf", "rg", "cargo", "telefone"]

        widgets = {
            "nome": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "NOME COMPLETO"
            }),
            "cpf": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "000.000.000-00"
            }),
            "rg": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "RG"
            }),
            "cargo": forms.Select(attrs={
                "class": "form-control"
            }),
            "telefone": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "(00) 00000-0000"
            }),
        }

class VeiculoForm(forms.ModelForm):
    class Meta:
        model = Veiculo
        fields = ["placa", "modelo", "combustivel"]
        
        widgets = {
            "placa": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "AAA1234"
            }),
            "modelo": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Digite o modelo da viatura"
            }),
            "combustivel": forms.Select(attrs={
                "class": "form-control"
            }),
        }