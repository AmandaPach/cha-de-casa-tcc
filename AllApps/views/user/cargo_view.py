from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from AllApps.models.user.cargo_models import Cargo
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View, DetailView

class CargoListView(ListView):
    model = Cargo
    template_name = 'Cargos/cargo_list.html'
    context_object_name = 'cargos'

class CargoCreateView(CreateView):
    model = Cargo
    template_name = 'Cargos/cargo_form.html'
    fields = [
      'nome_cargo', 'descricao_cargo', 'salario_base_cargo'
    ]
    success_url = reverse_lazy("cargo-list")

class CargoUpdateView(UpdateView):
    model = Cargo
    template_name = 'Cargos/cargo_form.html'
    fields = [
        'nome_cargo', 'descricao_cargo', 'salario_base_cargo'
    ]
    success_url = reverse_lazy("cargo-list")

class CargoDeleteView(DeleteView):
    model = Cargo
    template_name = 'Cargos/cargo_confirm_delete.html'
    success_url = reverse_lazy("cargo-list")