from django.shortcuts import render
from django.urls import reverse_lazy
from AllApps.models.caixa.formaPagamento_models import FormaPagamento
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View, DetailView

class FormaPagamentoListView(ListView):
    model = FormaPagamento
    template_name = 'FormasPagamento/formaPagamento_list.html'
    context_object_name = 'formasPagamento'

class FormaPagamentoCreateView(CreateView):
    model = FormaPagamento
    template_name = 'FormasPagamento/formaPagamento_form.html'
    fields = [
        'nome_forma_pgto', 'descricao_forma_pgto'
    ]
    success_url = reverse_lazy("formaPagamento-list")

class FormaPagamentoUpdateView(UpdateView):
    model = FormaPagamento
    template_name = 'FormasPagamento/formaPagamento_form.html'
    fields = [
        'nome_forma_pgto', 'descricao_forma_pgto'
    ]
    success_url = reverse_lazy("formaPagamento-list")

class FormaPagamentoDeleteView(DeleteView):
    model = FormaPagamento
    template_name = 'FormasPagamento/formaPagamento_confirm_delete.html'
    success_url = reverse_lazy("formaPagamento-list")