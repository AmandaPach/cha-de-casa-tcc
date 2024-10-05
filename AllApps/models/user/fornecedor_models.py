from django.db import models
from django.utils import timezone
from AllApps.models.cep.cidade_models import Cidade
from AllApps.models.cep.estado_models import Estado
        
class Fornecedor(models.Model):
    id_fornecedor = models.AutoField(primary_key=True, verbose_name="ID")
    razao_social_fornecedor = models.CharField(max_length=250, verbose_name="Razão Social")
    nome_fantasia_fornecedor = models.CharField(max_length=250, verbose_name="Nome Fantasia")
    cnpj_fornecedor = models.CharField(max_length=14, unique=True, verbose_name="CNPJ")
    ie_fornecedor = models.CharField(max_length=20, unique=True, verbose_name="IE")
    email_fornecedor = models.CharField(max_length=100, verbose_name="E-mail")
    data_fundacao_fornecedor = models.DateField(verbose_name="Data de Fundação")
    telefone_fornecedor = models.CharField(max_length=20, verbose_name="Telefone")
    limite_credito_fornecedor = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Limite de Crédito")
    rua_fornecedor = models.CharField(max_length=100, verbose_name="Rua")
    complemento_fornecedor = models.CharField(max_length=100, blank=True, null=True, verbose_name='Complemento')
    cep_fornecedor = models.CharField(max_length=10, verbose_name='CEP')
    numero_rua_fornecedor = models.CharField(max_length=10, verbose_name='Número')
    bairro_fornecedor = models.CharField(max_length=100, verbose_name='Bairro')
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE, null=True, blank=True, related_name='fornecedores', verbose_name="Cidade")
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE, null=True, blank=True, related_name='fornecedores', verbose_name="Estado")
    data_cadastro = models.DateTimeField(default=timezone.now, null=False, blank=False, verbose_name="Data Cadastro")
    data_ultima_alteracao = models.DateTimeField(auto_now=True, null=False, blank=False, verbose_name="Última Alteração")

    def __str__(self):
        return f"{self.razao_social_fornecedor} ({self.nome_fantasia_fornecedor} - {self.cnpj_fornecedor}"
    
    
    def save(self, *args, **kwargs):
        self.razao_social_fornecedor = self.razao_social_fornecedor.upper()
        self.nome_fantasia_fornecedor = self.nome_fantasia_fornecedor.upper()
        self.rua_fornecedor = self.rua_fornecedor.upper()
        self.bairro_fornecedor = self.bairro_fornecedor.upper()
        self.email_fornecedor = self.email_fornecedor.upper()
        if self.complemento_fornecedor:
            self.complemento_fornecedor = self.complemento_fornecedor.upper()
        super(Fornecedor, self).save(*args, **kwargs)
        
    class Meta: 
        db_table="Fornecedor"
        verbose_name_plural="Fornecedores"
        ordering = ["id_fornecedor"]