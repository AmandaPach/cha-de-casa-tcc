from django.db import models
from django.utils import timezone

class CondicaoPagamento(models.Model):

    id_condicao_pgto = models.AutoField(primary_key=True, verbose_name="ID")
    nome_condicao_pgto = models.CharField(max_length=100, verbose_name="Condição de Pagamento")
    descricao_condicao_pgto = models.TextField(max_length=200, verbose_name="Descrição")
    desconto_por_antecipacao_condicao_pgto = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Desconto por antecipação")
    juros_mensais_condicao_pgto = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Juros")
    data_cadastro = models.DateTimeField(default=timezone.now, null=False, blank=False, verbose_name="Data Cadastro")
    data_ultima_alteracao = models.DateTimeField(auto_now=True, null=False, blank=False, verbose_name="Última Alteração")
    
    def __str__(self):
        return f"{self.nome_condicao_pgto}"
    
    def save(self, *args, **kwargs):
        self.nome_condicao_pgto = self.nome_condicao_pgto.upper()
        if self.descricao_condicao_pgto:
            self.descricao_condicao_pgto = self.descricao_condicao_pgto.upper()
        super(CondicaoPagamento, self).save(*args, **kwargs)
        
    class Meta: 
        db_table="CondicaoPagamento"
        verbose_name_plural="Condições de Pagamento"
        ordering = ["id_condicao_pgto"]