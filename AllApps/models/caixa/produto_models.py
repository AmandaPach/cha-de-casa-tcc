from django.db import models
from django.utils import timezone
from AllApps.models.caixa.categoria_models import Categoria
from AllApps.models.caixa.tipo_models import Tipo
 
class Produto(models.Model):
    UNIMEDIDA_CHOICES = [
        ('KG', 'Kilograma'),
        ('L', 'Litros'),
        ('Uni', 'Unidade'),
    ]
    
    id_produto = models.AutoField(primary_key=True, verbose_name="ID")
    nome_produto = models.CharField(max_length=100, verbose_name="Produto")
    descricao_produto = models.CharField(max_length=200, blank=True, null=True, verbose_name="Descrição")
    preco_custo_produto = models.DecimalField(max_length=12, max_digits=10, decimal_places=2, blank=False, null=False, verbose_name="Preço de custo")
    preco_venda_produto = models.DecimalField(max_length=12, max_digits=10, decimal_places=2, blank=False, null=False, verbose_name="Preço de venda")
    preco_medio_produto = models.DecimalField(max_length=12, max_digits=10, decimal_places=2, blank=False, null=False, verbose_name="Preço médio")
    quantidade_produto = models.DecimalField(max_length=10, max_digits=10, default=0, decimal_places=3, blank=True, null=True, verbose_name="Quantidade")
    unid_medida_produto = models.CharField(max_length=5, choices=UNIMEDIDA_CHOICES, verbose_name="Unidade de medida")
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=False, blank=False, related_name='categorias', verbose_name="Categoria")
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE, null=False, blank=False, related_name='tipos', verbose_name="Tipo")
    data_cadastro = models.DateTimeField(default=timezone.now, null=False, blank=False, verbose_name="Data Cadastro")
    data_ultima_alteracao = models.DateTimeField(auto_now=True, null=False, blank=False, verbose_name="Última Alteração")
    
    
    def save(self, *args, **kwargs):
        self.nome_produto = self.nome_produto.upper()
        if self.descricao_produto:
            self.descricao_produto = self.descricao_produto.upper()
        
        super(Produto, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.nome_produto} ( {self.categoria} | {self.tipo} )"
    
        
    class Meta: 
        db_table="Produto"
        verbose_name_plural="Produtos"
        ordering = ["id_produto"]