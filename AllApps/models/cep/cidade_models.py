from django.db import models
from django.utils import timezone
from .estado_models import Estado

class Cidade(models.Model):
    id_cidade= models.AutoField(primary_key=True, verbose_name="ID")
    nome_cidade = models.CharField(max_length=100, null=False, blank=False, verbose_name="Cidade")
    ddd_cidade = models.CharField(max_length=3, null=False, blank=False, verbose_name="DDD")
    data_cadastro = models.DateTimeField(default=timezone.now, null=False, blank=False, verbose_name="Data Cadastro")
    data_ultima_alteracao = models.DateTimeField(auto_now=True, null=False, blank=False, verbose_name="Última Alteração")

    estado = models.ForeignKey(Estado, on_delete=models.CASCADE, null=False, blank=False, related_name='cidade', verbose_name="Estado")

    def __str__(self):
        return self.nome_cidade
    
    def save(self, *args, **kwargs):
        self.nome_cidade = self.nome_cidade.upper()
        super(Cidade, self).save(*args, **kwargs) 
    
    class Meta: 
        db_table="Cidade"
        verbose_name_plural="Cidades"
        ordering = ["id_cidade"]