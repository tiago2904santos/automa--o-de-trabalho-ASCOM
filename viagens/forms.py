from django import forms
from .models import Viajante, Veiculo, Oficio
from typing import cast

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



class OficioForm(forms.ModelForm):
   
    class Meta:
        model = Oficio
        fields = [
            'oficio', 'protocolo', 'sede', 'destino', 'servidor',
            'data_saida', 'data_chegada', 'valor_diaria', 'veiculo', 'motorista', 'motivo', 'status'
        ]
        widgets = {
            'data_saida': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'data_chegada': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'motivo': forms.Textarea(attrs={'rows': 4, 'class': 'form-control'}),
        }

    # Se você precisar manter os querysets personalizados (order_by), faça no __init__
    # Isso é uma boa prática para evitar problemas de cache no Django
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Aqui você "afirma" para o Pylance que o campo é um ModelChoiceField
        servidor_field = cast(forms.ModelChoiceField, self.fields['servidor'])
        servidor_field.queryset = Viajante.objects.all().order_by('nome')

        veiculo_field = cast(forms.ModelChoiceField, self.fields['veiculo'])
        veiculo_field.queryset = Veiculo.objects.all().order_by('modelo')

    def clean_data_chegada(self):
        # ... seu código de validação continua igual ...
        data_saida = self.cleaned_data.get('data_saida')
        data_chegada = self.cleaned_data.get('data_chegada')
        if data_saida and data_chegada:
            if data_chegada < data_saida:
                raise forms.ValidationError("A data de chegada não pode ser anterior à data de saída.")
        return data_chegada

  