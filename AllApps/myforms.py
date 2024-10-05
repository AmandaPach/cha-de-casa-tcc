from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field
from AllApps.models.cep.pais_models import Pais
from AllApps.models.cep.estado_models import Estado
from AllApps.models.cep.cidade_models import Cidade
from AllApps.models.user.cliente_models import Cliente
from AllApps.models.user.fornecedor_models import Fornecedor
from AllApps.models.user.cargo_models import Cargo
from AllApps.models.user.funcionario_models import Funcionario
from AllApps.models.caixa.formaPagamento_models import FormaPagamento
from AllApps.models.caixa.condicaoPagamento_models import CondicaoPagamento


class PaisForm(forms.ModelForm):
    class Meta:
        model = Pais
        fields = ['nome_pais', 'sigla_pais']
        error_messages = {
            'nome_pais': {
                'unique': "Este país já está cadastrado.",
            }
        }
    nome_pais = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Digite o nome do país'}),
    )  

    def clean_nome_pais(self):
        nome_pais = self.cleaned_data.get('nome_pais').upper()
        if Pais.objects.filter(nome_pais=nome_pais).exists():
            raise forms.ValidationError("Este país já está cadastrado.")
        return nome_pais

    def clean_sigla(self):
        sigla = self.cleaned_data.get('sigla').upper()
        return sigla
    
class EstadoForm(forms.ModelForm):
    class Meta:
        model = Estado
        fields = '__all__'
        error_messages = {
            'nome_estado': {
                'unique': "Este estado já está cadastrado.",
            }
        }
    nome_estado = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Digite o nome do estado'}),
    ) 

class FormaPagamentoForm(forms.ModelForm):
    class Meta:
        model = FormaPagamento
        fields = ['nome_forma_pgto', 'descricao_forma_pgto']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-FormaPagamentoForm'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = 'formaPagamento-create'
        self.helper.add_input(Submit('submit', 'Salvar'))

class CondicaoPagamentoForm(forms.ModelForm):
    class Meta:
        model = CondicaoPagamento
        fields = '__all__'

class FornecedorForm(forms.ModelForm):
    class Meta:
        model = Fornecedor
        fields = '__all__'

class CargoForm(forms.ModelForm):
    class Meta:
        model = Cargo
        fields = '__all__'

class FuncionarioForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = '__all__'