from django import forms
from .models import Viajante

class ViajanteForm(forms.ModelForm):
    class Meta:
        model = Viajante
        fields = ["nome", "cpf", "rg", "cargo", "telefone"]

        widgets = {
            "nome": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Nome completo"
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
