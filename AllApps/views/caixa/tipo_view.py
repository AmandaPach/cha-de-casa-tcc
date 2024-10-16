from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View, DetailView
from AllApps.models.caixa.tipo_models import Tipo
from AllApps.forms.caixa.tipo_forms import TipoForm
from django.db import IntegrityError
from django.contrib import messages


class TipoListView(ListView):
    model = Tipo
    template_name = 'Tipos/tipo_list.html'
    context_object_name = 'tipos'

class TipoCreateView(CreateView):
    model = Tipo
    template_name = 'Tipos/tipo_form.html'
    form_class = TipoForm
    success_url = reverse_lazy("tipo-list")

    def form_valid(self, form):
        try:
            return super().form_valid(form)
        except IntegrityError as e:
            if 'UNIQUE constraint' in str(e):
                form.add_error('nome_tipo', 'Já cadastrado')
                return self.form_invalid(form)
            else:
                raise e

class TipoUpdateView(UpdateView):
    model = Tipo
    template_name = 'Tipos/tipo_form.html'
    form_class = TipoForm
    success_url = reverse_lazy("tipo-list")

    def form_valid(self, form):
        try:
            return super().form_valid(form)
        except IntegrityError as e:
            if 'UNIQUE constraint' in str(e):
                form.add_error('nome_tipo', 'Já cadastrado')
                return self.form_invalid(form)
            else:
                raise e

class TipoDeleteView(DeleteView):
    model = Tipo
    template_name = 'Tipos/tipo_confirm_delete.html'
    success_url = reverse_lazy("tipo-list")