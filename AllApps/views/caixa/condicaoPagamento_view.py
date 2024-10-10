from django.shortcuts import render
from django.urls import reverse_lazy
from AllApps.models.caixa.condicaoPagamento_models import CondicaoPagamento
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View, DetailView
from django.db import IntegrityError

class CondicaoPagamentoListView(ListView):
    model = CondicaoPagamento
    template_name = 'CondicoesPagamento/condicaoPagamento_list.html'
    context_object_name = 'condicoesPagamento'

class CondicaoPagamentoCreateView(CreateView):
    model = CondicaoPagamento
    template_name = 'CondicoesPagamento/condicaoPagamento_form.html'
    fields = [
        'nome_condicao_pgto',
    ]
    success_url = reverse_lazy("condicaoPagamento-list")

    def form_valid(self, form):
        try:
            return super().form_valid(form)
        except IntegrityError as e:
            if 'UNIQUE constraint' in str(e):
                form.add_error('nome_condicao_pgto', 'Já cadastrado!')
                return self.form_invalid(form)
            else:
                raise e

class CondicaoPagamentoUpdateView(UpdateView):
    model = CondicaoPagamento
    template_name = 'CondicoesPagamento/condicaoPagamento_form.html'
    fields = [
        'nome_condicao_pgto',
    ]
    success_url = reverse_lazy("condicaoPagamento-list")

class CondicaoPagamentoDeleteView(DeleteView):
    model = CondicaoPagamento
    template_name = 'CondicoesPagamento/condicaoPagamento_confirm_delete.html'
    success_url = reverse_lazy("condicaoPagamento-list")