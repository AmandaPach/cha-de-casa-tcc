from django.db import models
from django.utils import timezone
from .pais_models import Pais

class Estado(models.Model):
    id_estado= models.AutoField(primary_key=True, verbose_name="ID")
    nome_estado = models.CharField(max_length=100, unique=True, null=False, blank=False, verbose_name="Estado")
    sigla_estado = models.CharField(max_length=3, null=True, blank=True, verbose_name="UF")
    data_cadastro = models.DateTimeField(default=timezone.now, null=False, blank=False, verbose_name="Data Cadastro")
    data_ultima_alteracao = models.DateTimeField(auto_now=True, null=False, blank=False, verbose_name="Última Alteração")

    pais = models.ForeignKey(Pais, on_delete=models.CASCADE, related_name='estado')

    def __str__(self):
        return f"{self.nome_estado} ({self.sigla_estado})"
    
    def save(self, *args, **kwargs):
        self.nome_estado = self.nome_estado.upper()
        if self.sigla_estado:
            self.sigla_estado = self.sigla_estado.upper()   
        super(Estado, self).save(*args, **kwargs)
    
    class Meta: 
        db_table="Estado"
        verbose_name_plural="Estados"
        ordering = ["id_estado"]