from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View, DetailView
from AllApps.models.caixa.produto_models import Produto
from AllApps.forms.caixa.produto_forms import ProdutoForm
from django.db import IntegrityError

class ProdutoListView(ListView):
    model = Produto
    template_name = 'Produtos/produto_list.html'
    context_object_name = 'produtos'

class ProdutoCreateView(CreateView):
    model = Produto
    template_name = 'Produtos/produto_form.html'
    form_class = ProdutoForm
    success_url = reverse_lazy("produto-list")

    def form_valid(self, form):
        try:
            return super().form_valid(form)
        except IntegrityError as e:
            if 'UNIQUE constraint' in str(e):
                form.add_error('nome_produto', 'Este produto já está cadastrado.')
                return self.form_invalid(form)
            else:
                raise e

class ProdutoUpdateView(UpdateView):
    model = Produto
    template_name = 'Produtos/produto_form.html'
    form_class = ProdutoForm
    success_url = reverse_lazy("produto-list")

    def form_valid(self, form):
        try:
            return super().form_valid(form)
        except IntegrityError as e:
            if 'UNIQUE constraint' in str(e):
                form.add_error('nome_produto', 'Este produto já está cadastrado.')
                return self.form_invalid(form)
            else:
                raise e

class ProdutoDeleteView(DeleteView):
    model = Produto
    template_name = 'Produtos/produto_confirm_delete.html'
    success_url = reverse_lazy("produto-list")