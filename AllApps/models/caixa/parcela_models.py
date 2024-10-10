from django.db import models
from django.utils import timezone
from AllApps.models.caixa.formaPagamento_models import FormaPagamento
from AllApps.models.caixa.condicaoPagamento_models import CondicaoPagamento


class Parcela(models.Model):
    id_parcela = models.AutoField(primary_key=True, verbose_name="ID")
    numero_parcela = models.PositiveIntegerField(verbose_name="Número da Parcela")
    dia_pgto_parcela = models.PositiveIntegerField(verbose_name="Dia do Pagamento")
    porcentagem_pgto_parcela = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Percentual Pago (%)")
    desconto_pgto_parcela = models.DecimalField(max_digits=5, decimal_places=2, default=0, verbose_name="Desconto")
    juros_pgto_parcela = models.DecimalField(max_digits=5, decimal_places=2, default=0, verbose_name="Juros")
    multa_pgto_parcela = models.DecimalField(max_digits=5, decimal_places=2, default=0, verbose_name="Multa")

    forma_pgto = models.ForeignKey(FormaPagamento, on_delete=models.CASCADE, verbose_name="Forma de Pagamento")
    condicao_pgto = models.ForeignKey(CondicaoPagamento, on_delete=models.CASCADE, related_name='condicaoPagamento', verbose_name="Condição de Pagamento")
    
    data_cadastro = models.DateTimeField(default=timezone.now, null=False, blank=False, verbose_name="Data Cadastro")
    data_ultima_alteracao = models.DateTimeField(auto_now=True, null=False, blank=False, verbose_name="Última Alteração")
    
    def __str__(self):
        return f"Parcela {self.numero_parcela} - {self.condicao_pgto.nome_condicao_pgto}"
        
    class Meta: 
        db_table="Parcela"
        verbose_name_plural="Parcelas"
        ordering = ["id_parcela"]