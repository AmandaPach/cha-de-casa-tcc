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
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Column(Field('nome_categoria', css_class='form-control'), css_class='col-md-6'),
                Column(Field('descricao_categoria', css_class='form-control'), css_class='col-md-6'),
                css_class='form-row'
            ),
            Submit('submit', 'Salvar', css_class='btn btn-primary')
        )