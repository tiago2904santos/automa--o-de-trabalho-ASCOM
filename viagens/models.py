from decimal import Decimal
from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User


# ================validação======================== #

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

placa_validator = RegexValidator(
    regex=r'^([A-Z]{3}[0-9]{4}|[A-Z]{3}[0-9][A-Z][0-9]{2})$',
    message='Placa inválida. Use o formato AAA1234 ou AAA1A23'
)



# =========== viajante ============ #

class Viajante(models.Model):
    CARGO_CHOICES = [
        ("Agente de Polícia Judiciária", "Agente de Polícia Judiciária"),
        ("Papiloscopista", "Papiloscopista"),
        ("Assessor", "Assessor"),
        ("Administrativo", "Administrativo"), 
        ("Delegado de Policia", "Delegado de Policia")
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
        choices=CARGO_CHOICES, 
        default="AGENTE DE POLÍCIA JUDICIÁRIA"
        )
    telefone = models.CharField(max_length=20, validators=[number_validator])

    def __str__(self):
        return f"{self.nome}"
    

    
# =========== veiculo ============ #

    
class Veiculo(models.Model):
    COMBUSTIVEL_CHOICES = [
        ("ETANOL", "Etanol"),
        ("GASOLINA", "Gasolina"),
        ("DIESEL", "Diesel"),
    ]

    placa = models.CharField(max_length=7, unique=True, validators=[placa_validator])
    modelo = models.CharField(max_length=20)
    combustivel = models.CharField(max_length=10, choices=COMBUSTIVEL_CHOICES)

    def __str__(self):
        return f"{self.placa} - {self.modelo}"
    

# ==============OFicio=======================================================

ESTADOS = [
        ('AC', 'Acre'),
        ('AL', 'Alagoas'),
        ('AP', 'Amapá'),
        ('AM', 'Amazonas'),
        ('BA', 'Bahia'),
        ('CE', 'Ceará'),
        ('DF', 'Distrito Federal'),
        ('ES', 'Espírito Santo'),
        ('GO', 'Goiás'),
        ('MA', 'Maranhão'),
        ('MT', 'Mato Grosso'),
        ('MS', 'Mato Grosso do Sul'),
        ('MG', 'Minas Gerais'),
        ('PA', 'Pará'),
        ('PB', 'Paraíba'),
        ('PR', 'Paraná'),
        ('PE', 'Pernambuco'),
        ('PI', 'Piauí'),
        ('RJ', 'Rio de Janeiro'),
        ('RN', 'Rio Grande do Norte'),
        ('RS', 'Rio Grande do Sul'),
        ('RO', 'Rondônia'),
        ('RR', 'Roraima'),
        ('SC', 'Santa Catarina'),
        ('SP', 'São Paulo'),
        ('SE', 'Sergipe'),
        ('TO', 'Tocantins'),
    ]


class Cidade(models.Model):
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=2, choices=ESTADOS)

    def __str__(self):
        return f"{self.cidade}/{self.estado}"

    @staticmethod
    def get_cidades_por_estado(estado):
        return Cidade.objects.filter(estado=estado).order_by('cidade')

    
class Oficio(models.Model):    

    # Oficio
    oficio = models.CharField(max_length=50)
    protocolo = models.CharField(max_length=50)
    # destino
    estado_sede = models.CharField(max_length=2, choices=ESTADOS, default="PR")
    cidade_sede = models.ForeignKey(Cidade, on_delete=models.SET_NULL, null=True, blank=True, related_name="sede_oficios")
    
    estado_destino = models.CharField(max_length=2, choices=ESTADOS, default="PR")
    cidade_destino = models.ForeignKey(Cidade, on_delete=models.SET_NULL, null=True, blank=True, related_name="destino_oficios")

    # Servidores
    servidor = models.ForeignKey(
        'Viajante',
        on_delete=models.CASCADE,
        related_name='oficios_servidor'  # <--- related_name único
    )
    motorista = models.ForeignKey(
        'Viajante',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='oficios_motorista'  # <--- related_name único
    )
    motorista_nome = models.CharField(max_length=255, blank=True)

    # Viagem
    data_saida = models.DateField()
    data_chegada = models.DateField()
    valor_diaria = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal("0.00"))
    veiculo = models.ForeignKey('Veiculo', on_delete=models.CASCADE)
    roteiro_ida = models.TextField(blank=True)
    roteiro_volta = models.TextField(blank=True)
    motivo = models.TextField()
    status = models.CharField(max_length=20, choices=[
        ('pendente', 'Pendente'),
        ('aprovado', 'Aprovado'),
        ('concluido', 'Concluído')
    ], default='pendente')

    def __str__(self):
        destino = self.cidade_destino or "Sem destino"
        return f"{self.oficio} - {self.servidor} - {destino}"


