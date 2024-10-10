from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Row, Column, Submit
from AllApps.models.caixa.condicaoPagamento_models import CondicaoPagamento

class CondicaoPagamentoForm(forms.ModelForm):
    class Meta:
        model = CondicaoPagamento
        fields = [
            'nome_condicao_pgto'
        ]
        help_texts = {
            'nome_condicao_pgto': 'Exemplo: 30 / 60 / 90 BB"',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'

        self.fields['nome_condicao_pgto'].widget.attrs.update({
            'style': 'text-transform: uppercase;',
            'class': 'form-control'
        })
     