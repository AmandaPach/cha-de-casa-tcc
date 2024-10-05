from django.shortcuts import render
from django.urls import reverse_lazy
from AllApps.models.user.fornecedor_models import Fornecedor
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View, DetailView

class FornecedorListView(ListView):
    model = Fornecedor
    template_name = 'Fornecedores/fornecedor_list.html'
    context_object_name = 'fornecedores'

class FornecedorCreateView(CreateView):
    model = Fornecedor
    template_name = 'Fornecedores/fornecedor_form.html'
    fields = [
        'razao_social_fornecedor', 'nome_fantasia_fornecedor', 'cnpj_fornecedor',
        'ie_fornecedor', 'data_fundacao_fornecedor', 'rua_fornecedor',
        'telefone_fornecedor', 'email_fornecedor', 'limite_credito_fornecedor',
        'complemento_fornecedor', 'cep_fornecedor', 'numero_rua_fornecedor',
        'bairro_fornecedor', 'cidade', 'estado'
   
    ]
    success_url = reverse_lazy("fornecedor-list")

class FornecedorUpdateView(UpdateView):
    model = Fornecedor
    template_name = 'Fornecedores/fornecedor_form.html'
    fields = [
        'razao_social_fornecedor', 'nome_fantasia_fornecedor', 'cnpj_fornecedor',
        'ie_fornecedor', 'data_fundacao_fornecedor', 'rua_fornecedor',
        'telefone_fornecedor', 'email_fornecedor', 'limite_credito_fornecedor',
        'complemento_fornecedor', 'cep_fornecedor', 'numero_rua_fornecedor',
        'bairro_fornecedor', 'cidade', 'estado'
    ]
    success_url = reverse_lazy("fornecedor-list")

class FornecedorDeleteView(DeleteView):
    model = Fornecedor
    template_name = 'Fornecedores/fornecedor_confirm_delete.html'
    success_url = reverse_lazy("fornecedor-list")