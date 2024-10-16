from django.db import models
from django.utils import timezone
from AllApps.models.user.fornecedor_models import Fornecedor
from AllApps.models.caixa.produto_models import Produto
 
class Compras(models.Model):
    class Meta: 
        db_table="Compra"
        verbose_name_plural="Compras"
        unique_together = (('nota_fiscal_compra', 'modelo_nota_compra', 'serie_compra'),)

        ordering = ["data_chegada"]

    def __str__(self):
        return f"{self.nota_fiscal_compra}{self.modelo_nota_compra}{self.serie_compra}"
    
    id_compra = models.AutoField(primary_key=True, verbose_name="ID")
    nota_fiscal_compra =  models.PositiveIntegerField(verbose_name="Nota Fiscal")
    modelo_nota_compra = models.PositiveIntegerField(verbose_name="Modelo Nota")
    serie_compra = models.PositiveIntegerField(verbose_name="Série")
    quantidade = models.PositiveIntegerField(verbose_name="Quantidade")
    custo = models.PositiveIntegerField(verbose_name="Custo")
    desconto = models.PositiveIntegerField(verbose_name="Desconto")
    valor_total = models.PositiveIntegerField(verbose_name="Valor Total")
    data_chegada = models.DateTimeField(default=timezone.now, null=False, blank=False, verbose_name="Data Chegada")
    data_emissao = models.DateTimeField(auto_now=True, null=False, blank=False, verbose_name="Data Emissão")   
    fornecedor = models.ForeignKey(Fornecedor,on_delete=models.CASCADE, verbose_name="Fornecedor")
    produto = models.ForeignKey(Produto,on_delete=models.CASCADE, verbose_name="Produto")
    data_cadastro = models.DateTimeField(default=timezone.now, null=False, blank=False, verbose_name="Data Cadastro")
    data_ultima_alteracao = models.DateTimeField(auto_now=True, null=False, blank=False, verbose_name="Última Alteração")

    def save(self, *args, **kwargs):
        self.id = f"{self.nota_fiscal_compra}{self.modelo_nota_compra}{self.serie_compra}"
        
        super(Compras, self).save(*args, **kwargs)