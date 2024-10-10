from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Row, Column, Submit
from AllApps.models.caixa.categoria_models import Categoria

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = [
            'nome_categoria', 'descricao_categoria', 
        ]

        help_texts = {
            'nome_categoria': 'Digite o nome da categoria. Ex: "Bebida", "Sobremesa", etc.',
            'descricao_categoria': 'Descreva brevemente a categoria de produto.',
        }

        widgets = {
            'descricao_categoria': forms.Textarea(attrs={
                'rows': 4,  # Altura do campo
                'cols': 40,  # Largura do campo
            }),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'

        # Adicionando o estilo de uppercase enquanto o usuário digita
        self.fields['nome_categoria'].widget.attrs.update({
            'style': 'text-transform: uppercase;',
            'class': 'form-control'
        })
        self.fields['descricao_categoria'].widget.attrs.update({
            'style': 'text-transform: uppercase;',
            'class': 'form-control'
        })