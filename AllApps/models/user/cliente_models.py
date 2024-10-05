from django.db import models
from django.utils import timezone
from cpf_field.models import CPFField
import re
from AllApps.models.cep.cidade_models import Cidade
from AllApps.models.cep.estado_models import Estado

 
class Cliente(models.Model):
    SEXO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('Outro', 'Outro'),
    ]

    id_cliente = models.AutoField(primary_key=True, verbose_name="ID")
    nome_cliente = models.CharField(max_length=100, verbose_name="Nome")
    sobrenome_cliente = models.CharField(max_length=100, verbose_name="Sobrenome")
    sexo_cliente = models.CharField(max_length=5, choices=SEXO_CHOICES, verbose_name="Sexo")
    telefone_cliente = models.CharField(max_length=15, verbose_name="Telefone")
    data_nascimento_cliente = models.DateField(verbose_name="Data de Nascimento")
    cpf_cliente = CPFField(max_length=14, null=False, blank=False, unique=True, verbose_name="CPF")
    rg_cliente = models.CharField(max_length=20, null=False, blank=False, unique=True, verbose_name="RG")
    rua_cliente = models.CharField(max_length=100, verbose_name="Rua")
    cep_cliente = models.CharField(max_length=10, verbose_name="CEP")
    bairro_cliente = models.CharField(max_length=100, verbose_name="Logradouro")
    numero_rua_cliente = models.CharField(max_length=10, verbose_name="Número")
    complemento_cliente = models.CharField(max_length=100, blank=True, null=True, verbose_name="Complemento")
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE, null=False, blank=False, related_name='clientes', verbose_name="Cidade")
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE, null=False, blank=False, related_name='clientes', verbose_name="Estado")
    data_cadastro = models.DateTimeField(default=timezone.now, null=False, blank=False, verbose_name="Data Cadastro")
    data_ultima_alteracao = models.DateTimeField(auto_now=True, null=False, blank=False, verbose_name="Última Alteração")
    
    
    def save(self, *args, **kwargs):
        self.nome_cliente = self.nome_cliente.upper()
        self.sobrenome_cliente = self.sobrenome_cliente.upper()
        self.rua_cliente = self.rua_cliente.upper()
        self.bairro_cliente = self.bairro_cliente.upper()
        if self.complemento_cliente:
            self.complemento_cliente = self.complemento_cliente.upper()
        
        # Remove qualquer caractere que não seja um dígito
        cpf_numeros = re.sub(r'\D', '', self.cpf_cliente)
        rg_numeros = re.sub(r'\D', '', self.rg_cliente)

        # Formata o CPF
        self.cpf_cliente = f'{cpf_numeros[:3]}.{cpf_numeros[3:6]}.{cpf_numeros[6:9]}-{cpf_numeros[9:]}'
        self.rg_cliente = f'{rg_numeros[:2]}.{rg_numeros[2:5]}.{rg_numeros[5:8]}-{rg_numeros[8:]}'   
        
        super(Cliente, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.nome_cliente} {self.sobrenome_cliente}"
    
        
    class Meta: 
        db_table="Cliente"
        verbose_name_plural="Clientes"
        ordering = ["id_cliente"]