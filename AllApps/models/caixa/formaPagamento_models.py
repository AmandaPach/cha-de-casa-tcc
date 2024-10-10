from django.db import models
from django.utils import timezone

class FormaPagamento(models.Model):

    id_forma_pgto = models.AutoField(primary_key=True, verbose_name="ID")
    nome_forma_pgto = models.CharField(max_length=20, null=False, blank=False, verbose_name="Forma de Pagamento")
    descricao_forma_pgto = models.TextField(max_length=50, null=True, blank=True, verbose_name="Descrição")

    data_cadastro = models.DateTimeField(default=timezone.now, null=False, blank=False, verbose_name="Data Cadastro")
    data_ultima_alteracao = models.DateTimeField(auto_now=True, null=False, blank=False, verbose_name="Última Alteração")
    
    def save(self, *args, **kwargs):
        self.nome_forma_pgto = self.nome_forma_pgto.upper()
        if self.descricao_forma_pgto:
            self.descricao_forma_pgto = self.descricao_forma_pgto.upper()
        super(FormaPagamento, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.nome_forma_pgto}"
    
    class Meta: 
        db_table="FormaPagamento"
        verbose_name_plural="Formas de Pagamento"
        ordering = ["id_forma_pgto"]