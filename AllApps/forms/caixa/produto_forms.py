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

        help_texts = {
            'nome_produto': 'Digite o nome do produto. Ex: "Bolo de cenoura"',
            'descricao_produto': 'Descreva brevemente o produto',
            'preco_custo_produto': 'Preço que você pagou pelo produto',
            'preco_venda_produto': 'Preço que você venderá o produto',
            'preco_medio_produto': 'Preço médio dos produtos similares',
            'quantidade_produto': 'Quantidade disponível',
            'unid_medida_produto': 'Unidade de medida do produto. Ex: Kg, Uni',
        }

        widgets = {
            'descricao_produto': forms.Textarea(attrs={
                'rows': 4,  # Altura do campo
                'cols': 40,  # Largura do campo
            }),
        }

    def clean_preco_custo_produto(self):
        preco_custo = self.cleaned_data.get('preco_custo_produto')
        if preco_custo <= 0:
            raise forms.ValidationError('O preço de custo não pode ser zero ou negativo.')
        return preco_custo

    def clean_preco_venda_produto(self):
        preco_venda = self.cleaned_data.get('preco_venda_produto')
        if preco_venda <= 0:
            raise forms.ValidationError('O preço de venda não pode ser zero ou negativo.')
        return preco_venda

    def clean_preco_medio_produto(self):
        preco_medio = self.cleaned_data.get('preco_medio_produto')
        if preco_medio <= 0:
            raise forms.ValidationError('O preço médio não pode ser zero ou negativo.')
        return preco_medio
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        
      # Campos de preço com máscara
        self.fields['preco_custo_produto'].widget.attrs.update({
            'id': 'preco_custo',
            'class': 'form-control',
            'min': '0',  # Impede a entrada de valores negativos
            'onkeypress': 'return event.charCode >= 48 && event.charCode <= 57'  # Permite apenas dígitos
        })
        self.fields['preco_venda_produto'].widget.attrs.update({
            'id': 'preco_venda',
            'class': 'form-control',
            'min': '0',  # Impede a entrada de valores negativos
            'onkeypress': 'return event.charCode >= 48 && event.charCode <= 57'  # Permite apenas dígitos
        })
        self.fields['preco_medio_produto'].widget.attrs.update({
            'id': 'preco_medio',
            'class': 'form-control',
            'min': '0',  # Impede a entrada de valores negativos
            'onkeypress': 'return event.charCode >= 48 && event.charCode <= 57'  # Permite apenas dígitos
        })
        self.fields['quantidade_produto'].widget.attrs.update({
            'id': 'quantidade',
            'class': 'form-control',
            'min': '0',  # Impede a entrada de valores negativos
            'onkeypress': 'return event.charCode >= 48 && event.charCode <= 57'  # Permite apenas dígitos
        })              