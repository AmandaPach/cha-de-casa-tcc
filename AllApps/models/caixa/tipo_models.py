from django.db import models
from django.utils import timezone
 
class Tipo(models.Model):

    id_tipo = models.AutoField(primary_key=True, verbose_name="ID")
    nome_tipo = models.CharField(max_length=100, verbose_name="Tipo")
    descricao_tipo = models.CharField(max_length=200, verbose_name="Descrição")
    data_cadastro = models.DateTimeField(default=timezone.now, null=False, blank=False, verbose_name="Data Cadastro")
    data_ultima_alteracao = models.DateTimeField(auto_now=True, null=False, blank=False, verbose_name="Última Alteração")
    
    
    def save(self, *args, **kwargs):
        self.nome_tipo = self.nome_tipo.upper()
        if self.descricao_tipo:
            self.descricao_tipo = self.descricao_tipo.upper()
        
        super(Tipo, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.nome_tipo}"
    
        
    class Meta: 
        db_table="Tipo"
        verbose_name_plural="Tipos"
        ordering = ["id_tipo"]