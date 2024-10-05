from django.db import models
from django.utils import timezone

class Cargo(models.Model):

    id_cargo = models.AutoField(primary_key=True, verbose_name="ID")
    nome_cargo = models.CharField(max_length=100, verbose_name="Cargo")
    descricao_cargo = models.CharField(max_length=100, verbose_name="Descrição")
    salario_base_cargo = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Salário")
    data_cadastro = models.DateTimeField(default=timezone.now, null=False, blank=False, verbose_name="Data Cadastro")
    data_ultima_alteracao = models.DateTimeField(auto_now=True, null=False, blank=False, verbose_name="Última Alteração")
    
    def __str__(self):
        return f"{self.nome_cargo} {self.salario_base_cargo}"
    
    def save(self, *args, **kwargs):
        self.nome_cargo = self.nome_cargo.upper()
        self.descricao_cargo = self.descricao_cargo.upper()
        if self.descricao_cargo:
            self.descricao_cargo = self.descricao_cargo.upper()
        super(Cargo, self).save(*args, **kwargs)

    class Meta: 
        db_table="Cargo"
        verbose_name_plural="Cargos"
        ordering = ["id_cargo"]