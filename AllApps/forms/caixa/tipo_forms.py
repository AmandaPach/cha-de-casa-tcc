from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Row, Column, Submit, HTML
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
                'class': 'form-control',
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Se existir uma instância, habilitar os campos como somente leitura 'id_tipo', data_ultima_alteracao' e data_cadastro'
        if self.instance and self.instance.pk:
            self.fields['id_tipo'] = forms.DateTimeField(
                widget=forms.TextInput(attrs={'readonly': 'readonly', 'disabled': 'disabled', 'class': 'form-control'}),
                initial=self.instance.id_tipo
            )

            self.fields['data_ultima_alteracao'] = forms.DateTimeField(
                widget=forms.TextInput(attrs={'readonly': 'readonly', 'disabled': 'disabled', 'class': 'form-control'}),
                initial=self.instance.data_ultima_alteracao
            )

            # Adicionar o campo 'data_cadastro' como somente leitura
            self.fields['data_cadastro'] = forms.DateTimeField(
                widget=forms.TextInput(attrs={'readonly': 'readonly', 'disabled': 'disabled', 'class': 'form-control'}),
                initial=self.instance.data_cadastro
            )
        else:
            # Remover 'id_tipo', 'data_ultima_alteracao' e 'data_cadastro' se for um novo registro
            del self.fields['data_cadastro']
    
        self.helper = FormHelper()
        self.helper.form_method = 'post'

        # Definindo a ordem dos campos manualmente
        if self.instance and self.instance.pk:
            # Se for edição, incluir 'id_tipo', 'data_ultima_alteracao' e data_cadastro'
            self.helper.layout = Layout(
                Field('id_tipo', css_class='form-control', placeholder=self.fields['id_tipo'].label),
                Field('nome_tipo', css_class='form-control', placeholder=self.fields['nome_tipo'].label),
                Field('nome_tipo', css_class='form-control', placeholder=self.fields['nome_tipo'].label),
                Field('descricao_tipo', css_class='form-control', placeholder=self.fields['descricao_tipo'].label),
                Field('data_cadastro', css_class='form-control', placeholder=self.fields['data_cadastro'].label),
                Field('data_ultima_alteracao', css_class='form-control', placeholder=self.fields['data_ultima_alteracao'].label),
                Submit('submit', 'Salvar')
            )
        else:
            # Se for novo registro, não exibir 'id_tipo', 'data_ultima_alteracao' e data_cadastro'
            self.helper.layout = Layout(
                Field('nome_tipo', css_class='form-control', placeholder=self.fields['nome_tipo'].label),
                Field('descricao_tipo', css_class='form-control', placeholder=self.fields['descricao_tipo'].label),
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