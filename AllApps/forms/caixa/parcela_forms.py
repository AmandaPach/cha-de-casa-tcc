from django import forms
from django.forms import inlineformset_factory
from AllApps.models.caixa.parcela_models import Parcela
from AllApps.models.caixa.condicaoPagamento_models import CondicaoPagamento

class ParcelaForm(forms.ModelForm):
    class Meta:
        model = Parcela
        fields = [
            'numero_parcela', 'dia_pgto_parcela'
        ]

# Criação do formset para as parcelas
ParcelaFormSet = inlineformset_factory(
    CondicaoPagamento, Parcela, form=ParcelaForm, extra=1, can_delete=True
)