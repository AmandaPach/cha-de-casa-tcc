from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Row, Column, Submit
from AllApps.models.caixa.tipo_models import Tipo

class TipoForm(forms.ModelForm):
    class Meta:
        model = Tipo
        fields = [
            'nome_tipo', 'descricao_tipo', 
        ]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Column(Field('nome_tipo', css_class='form-control'), css_class='col-md-6'),
                Column(Field('descricao_tipo', css_class='form-control'), css_class='col-md-6'),
                css_class='form-row'
            ),
            Submit('submit', 'Salvar', css_class='btn btn-primary')
        )