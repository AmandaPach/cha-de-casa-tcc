from django.db import models
from django.utils import timezone

class CondicaoPagamento(models.Model):
    id_condicao_pgto = models.AutoField(primary_key=True, verbose_name="ID")
    nome_condicao_pgto = models.CharField(max_length=20, null=False, blank=False, verbose_name="Condição de Pagamento")
    data_cadastro = models.DateTimeField(default=timezone.now, null=False, blank=False, verbose_name="Data Cadastro")
    data_ultima_alteracao = models.DateTimeField(auto_now=True, null=False, blank=False, verbose_name="Última Alteração")

    def save(self, *args, **kwargs):
        self.nome_condicao_pgto = self.nome_condicao_pgto.upper()
        super(CondicaoPagamento, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.nome_condicao_pgto}"    
        
    class Meta: 
        db_table="CondicaoPagamento"
        verbose_name_plural="Condições de Pagamento"
        ordering = ["id_condicao_pgto"]