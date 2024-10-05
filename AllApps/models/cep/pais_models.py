from django.db import models
from django.utils import timezone

class Pais(models.Model):
    id_pais = models.AutoField(primary_key=True, verbose_name="ID")
    nome_pais = models.CharField(max_length=100, null=False, blank=False, unique=True, verbose_name="Pais")
    sigla_pais = models.CharField(max_length=3, null=True, blank=True, verbose_name="Sigla")
    data_cadastro = models.DateTimeField(default=timezone.now, null=False, blank=False, verbose_name="Data Cadastro")
    data_ultima_alteracao = models.DateTimeField(auto_now=True, null=False, blank=False, verbose_name="Última Alteração")

    def __str__(self):
        return self.nome_pais
    
    def save(self, *args, **kwargs):
        if self.nome_pais:
            self.nome_pais = self.nome_pais.upper()
        if self.sigla_pais:
            self.sigla_pais = self.sigla_pais.upper()
        super(Pais, self).save(*args, **kwargs) 
        
    class Meta: 
        db_table="Pais"
        verbose_name_plural="Paises"
        ordering = ["id_pais"]