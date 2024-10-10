from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Row, Column, Submit
from AllApps.models.caixa.tipo_models import Tipo

class TipoForm(forms.ModelForm):
    class Meta:
        model = Tipo
        fields = [
            'id_tipo','nome_tipo', 'descricao_tipo', 'data_cadastro'
        ]
        help_texts = {
            'nome_tipo': 'Digite o nome do tipo. Ex: "Insumo", "Produto final", etc.',
            'descricao_tipo': 'Descreva brevemente o tipo de produto.',
        }
        widgets = {
            'descricao_tipo': forms.Textarea(attrs={
                'rows': 4,  # Altura do campo
                'cols': 40,  # Largura do campo
            }),
            'id_tipo': forms.TextInput(attrs={'readonly': 'readonly'}),
            'data_criacao': forms.TextInput(attrs={'readonly': 'readonly'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Sempre mostrar o id bloqueado
        self.fields['id_tipo'] = forms.CharField(
            widget=forms.TextInput(attrs={'readonly': 'readonly', 'disabled': 'disabled'}),
        )

        # Se existir uma instância, inicialize o valor do id_tipo
        if self.instance and self.instance.pk:
            self.fields['id_tipo'].initial = self.instance.id_tipo
        
        if self.instance and self.instance.pk:
            self.fields['id_tipo'] = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly', 'disabled': 'disabled'}))
            self.fields['id_tipo'].initial = self.instance.id_tipo

        # Desabilitar o campo 'data_cadastro'
        self.fields['data_cadastro'].widget.attrs['readonly'] = True
        self.fields['data_cadastro'].disabled = True

        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Salvar'))

        # Definindo a ordem dos campos manualmente
        self.helper.layout = Layout(
            Field('id_tipo'), 
            Field('nome_tipo'),
            Field('descricao_tipo'),
            Field('data_cadastro'),
            Submit('submit', 'Salvar')
        )
        # Adicionando o estilo de uppercase enquanto o usuário digita
        self.fields['nome_tipo'].widget.attrs.update({
            'style': 'text-transform: uppercase;',
            'class': 'form-control'
        })
        self.fields['descricao_tipo'].widget.attrs.update({
            'style': 'text-transform: uppercase;',
            'class': 'form-control'
        })