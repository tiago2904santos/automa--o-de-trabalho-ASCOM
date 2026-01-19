from django.db import models
from django.core.validators import RegexValidator

cpf_validator = RegexValidator(
    regex=r'^\d{3}\.\d{3}\.\d{3}-\d{2}$',
    message='CPF deve estar no formato XXX.XXX.XXX-XX'
)

rg_validator = RegexValidator(
    regex=r'^[0-9A-Za-z\.\-]+$',
    message='RG inválido'
)

placa_validator = RegexValidator(
    regex=r'^([A-Z]{3}[0-9]{4}|[A-Z]{3}[0-9][A-Z][0-9]{2})$',
    message='Placa inválida (formatos aceitos: AAA1234 ou AAA1A23)'
)

number_validator = RegexValidator(
    regex = r'^\(\d{2}\)\s\d{4,5}-\d{4}$',
    message='Telefone inválido. Use o formato (DD) XXXXX-XXXX'
)

protocol_validator = RegexValidator(

)


class Viajante(models.Model):
    CARGO_CHOICES = [
        ("AGENTE DE POLÍCIA JUDICIÁRIA", "Agente de Polícia Judiciária"),
        ("PAPILOSCOPISTA", "Papiloscopista"),
        ("ASSESSOR", "Assessor"),
        ("ADMINISTRATIVO", "Administrativo"), 
    ]

    nome = models.CharField(max_length=255)
    rg = models.CharField(
    max_length=20,
    unique=True,
    null=True,      
    blank=True,     
    validators=[rg_validator]
    )

    cpf = models.CharField(max_length=14, unique=True, validators=[cpf_validator])
    cargo = models.CharField(
        max_length=100, 
        choices=CARGO_CHOICES, 
        default="AGENTE DE POLÍCIA JUDICIÁRIA"
        )
    telefone = models.CharField(max_length=20, validators=[number_validator])

    def __str__(self):
        return f"{self.nome}"
    

class Veiculo(models.Model):

    COMBUSTIVEL_CHOICES = [
        ('GASOLINA', 'Gasolina'),
        ('ETANOL', 'Etanol'),
        ('DIESEL', 'Diesel'),
    ]

    placa = models.CharField(
        max_length=7,
        unique=True,
        validators=[placa_validator]
    )
    modelo = models.CharField(max_length=100)
    combustivel = models.CharField(
        max_length=10, 
        choices=COMBUSTIVEL_CHOICES,
        default="ETANOL")

    def __str__(self):
        return f" {self.modelo} - {self.placa}"
    

