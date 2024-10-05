from django.shortcuts import render
from django.urls import reverse_lazy
from AllApps.models.user.cliente_models import Cliente
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View, DetailView
from AllApps.forms.user.cliente_forms import ClienteForm
from django.db import IntegrityError

class ClienteListView(ListView):
    model = Cliente
    template_name = 'Clientes/cliente_list.html'
    context_object_name = 'clientes'

class ClienteCreateView(CreateView):
    model = Cliente
    template_name = 'Clientes/cliente_form.html'
    form_class = ClienteForm
    success_url = reverse_lazy("cliente-list")

    def form_valid(self, form):
        try:
            return super().form_valid(form)
        except IntegrityError as e:
            if 'UNIQUE constraint' in str(e):
                form.add_error('cpf_cliente', 'Este CPF já está cadastrado.')
                return self.form_invalid(form)
            else:
                raise e

class ClienteUpdateView(UpdateView):
    model = Cliente
    template_name = 'Clientes/cliente_form.html'
    form_class = ClienteForm
    success_url = reverse_lazy("cliente-list")

    def form_valid(self, form):
        try:
            return super().form_valid(form)
        except IntegrityError as e:
            if 'UNIQUE constraint' in str(e):
                form.add_error('cpf_cliente', 'Este CPF já está cadastrado.')
                return self.form_invalid(form)
            else:
                raise e

class ClienteDeleteView(DeleteView):
    model = Cliente
    template_name = 'Clientes/cliente_confirm_delete.html'
    success_url = reverse_lazy("cliente-list")