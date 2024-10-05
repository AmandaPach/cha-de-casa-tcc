from django.db import models
from django.utils import timezone
from AllApps.models.user.cargo_models import Cargo
       
class Funcionario(models.Model):
    SEXO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('Outro', 'Outro'),
    ]

    id_funcionario = models.AutoField(primary_key=True, verbose_name="ID")
    nome_funcionario = models.CharField(max_length=100, verbose_name="Nome")
    sobrenome_funcionario = models.CharField(max_length=100, verbose_name="Sobrenome")
    sexo_funcionario = models.CharField(max_length=5, choices=SEXO_CHOICES, verbose_name="Sexo")
    cpf_funcionario = models.CharField(max_length=14, unique=True, verbose_name="CPF")
    rg_funcionario = models.CharField(max_length=20, unique=True, verbose_name="RG")
    telefone_funcionario = models.CharField(max_length=14, verbose_name="Telefone")
    data_nascimento_funcionario = models.DateField(max_length=10,verbose_name="Data de Nascimento")
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE, null=True, blank=True, related_name='funcionarios', verbose_name="Cargo")
    data_cadastro = models.DateTimeField(default=timezone.now, null=False, blank=False, verbose_name="Data Cadastro")
    data_ultima_alteracao = models.DateTimeField(auto_now=True, null=False, blank=False, verbose_name="Última Alteração")
    
    def __str__(self):
        return f"{self.nome_funcionario} {self.sobrenome_funcionario} - {self.cargo}"
    
    def save(self, *args, **kwargs):
        self.nome_funcionario = self.nome_funcionario.upper()
        self.sobrenome_funcionario = self.sobrenome_funcionario.upper()
        super(Funcionario, self).save(*args, **kwargs)
        
    class Meta: 
        db_table="Funcionario"
        verbose_name_plural="Funcionarios"
        ordering = ["id_funcionario"]