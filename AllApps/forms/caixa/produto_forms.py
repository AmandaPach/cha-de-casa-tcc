from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Row, Column, Submit
from AllApps.models.caixa.produto_models import Produto

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = [
            'nome_produto', 'descricao_produto', 
            'preco_custo_produto', 'preco_venda_produto', 'preco_medio_produto', 
            'unid_medida_produto', 'quantidade_produto', 'categoria', 'tipo'
        ]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Column(Field('nome_produto', css_class='form-control'), css_class='col-md-6'),
                Column(Field('descricao_produto', css_class='form-control'), css_class='col-md-6'),
                css_class='form-row'
            ),
            Row(
                Column('unid_medida_produto', css_class='form-group col-md-2'),
                Column('quantidade_produto', css_class='form-group col-md-2'),
                Column('preco_custo_produto', css_class='form-group col-md-2'),
                Column('preco_venda_produto', css_class='form-group col-md-2'),
                Column('preco_medio_produto', css_class='form-group col-md-2'),
                css_class='form-row'
            ),
            Row(
                Column('categoria', css_class='form-group col-md-6'),
                Column('tipo', css_class='form-group col-md-6'),
                css_class='form-row'
            ),
            Submit('submit', 'Salvar', css_class='btn btn-primary')
        )