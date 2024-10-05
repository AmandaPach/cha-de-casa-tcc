from django.db import models
from django.utils import timezone
 
class Categoria(models.Model):

    id_categoria = models.AutoField(primary_key=True, verbose_name="ID")
    nome_categoria = models.CharField(max_length=100, verbose_name="Categoria")
    descricao_categoria = models.CharField(max_length=200, verbose_name="Descrição")
    data_cadastro = models.DateTimeField(default=timezone.now, null=False, blank=False, verbose_name="Data Cadastro")
    data_ultima_alteracao = models.DateTimeField(auto_now=True, null=False, blank=False, verbose_name="Última Alteração")
    
    
    def save(self, *args, **kwargs):
        self.nome_categoria = self.nome_categoria.upper()
        if self.descricao_categoria:
            self.descricao_categoria = self.descricao_categoria.upper()
        
        super(Categoria, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.nome_categoria}"
    
        
    class Meta: 
        db_table="Categoria"
        verbose_name_plural="Categorias"
        ordering = ["id_categoria"]