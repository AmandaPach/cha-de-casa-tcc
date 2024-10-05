from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View, DetailView
from AllApps.models.caixa.categoria_models import Categoria
from AllApps.forms.caixa.categoria_forms import CategoriaForm
from django.db import IntegrityError

class CategoriaListView(ListView):
    model = Categoria
    template_name = 'Categorias/categoria_list.html'
    context_object_name = 'categorias'

class CategoriaCreateView(CreateView):
    model = Categoria
    template_name = 'Categorias/categoria_form.html'
    form_class = CategoriaForm
    success_url = reverse_lazy("categoria-list")

    def form_valid(self, form):
        try:
            return super().form_valid(form)
        except IntegrityError as e:
            if 'UNIQUE constraint' in str(e):
                form.add_error('nome_categoria', 'Este categoria já está cadastrado.')
                return self.form_invalid(form)
            else:
                raise e

class CategoriaUpdateView(UpdateView):
    model = Categoria
    template_name = 'Categorias/categoria_form.html'
    form_class = CategoriaForm
    success_url = reverse_lazy("categoria-list")

    def form_valid(self, form):
        try:
            return super().form_valid(form)
        except IntegrityError as e:
            if 'UNIQUE constraint' in str(e):
                form.add_error('nome_categoria', 'Este categoria já está cadastrado.')
                return self.form_invalid(form)
            else:
                raise e

class CategoriaDeleteView(DeleteView):
    model = Categoria
    template_name = 'Categorias/categoria_confirm_delete.html'
    success_url = reverse_lazy("categoria-list")