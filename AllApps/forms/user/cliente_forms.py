from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Row, Column, Submit
from AllApps.models.user.cliente_models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = [
            'nome_cliente', 'sobrenome_cliente', 'sexo_cliente', 
            'telefone_cliente', 'data_nascimento_cliente', 
            'cpf_cliente', 'rg_cliente', 'rua_cliente', 
            'cep_cliente', 'bairro_cliente', 'numero_rua_cliente', 
            'complemento_cliente', 'cidade', 'estado'
        ]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Column(Field('nome_cliente', css_class='form-control'), css_class='col-md-6'),
                Column(Field('sobrenome_cliente', css_class='form-control'), css_class='col-md-6'),
                css_class='form-row'
            ),
            Row(
                Column('sexo_cliente', css_class='form-group col-md-4'),
                Column('telefone_cliente', css_class='form-group col-md-4'),
                Column('data_nascimento_cliente', css_class='form-group col-md-4'),
                css_class='form-row'
            ),
            Row(
                Column('cpf_cliente', css_class='form-group col-md-6'),
                Column('rg_cliente', css_class='form-group col-md-6'),
                css_class='form-row'
            ),
            Row(
                Column('rua_cliente', css_class='form-group col-md-6'),
                Column('numero_rua_cliente', css_class='form-group col-md-6'),
                css_class='form-row'
            ),
            Row(
                Column('bairro_cliente', css_class='form-group col-md-6'),
                Column('complemento_cliente', css_class='form-group col-md-6'),
                css_class='form-row'
            ),
            Row(
                Column('cep_cliente', css_class='form-group col-md-6'),
                Column('cidade', css_class='form-group col-md-3'),
                Column('estado', css_class='form-group col-md-3'),
                css_class='form-row'
            ),
            Submit('submit', 'Salvar', css_class='btn btn-primary')
        )