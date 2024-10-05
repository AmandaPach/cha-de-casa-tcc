from django.shortcuts import render
from django.urls import reverse_lazy
from AllApps.models.user.funcionario_models import Funcionario
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View, DetailView

class FuncionarioListView(ListView):
    model = Funcionario
    template_name = 'Funcionarios/funcionario_list.html'
    context_object_name = 'funcionarios'

class FuncionarioCreateView(CreateView):
    model = Funcionario
    template_name = 'Funcionarios/funcionario_form.html'
    fields = [
        'nome_funcionario', 'sobrenome_funcionario', 'sexo_funcionario', 'telefone_funcionario', 'data_nascimento_funcionario', 
        'cpf_funcionario', 'rg_funcionario', 'cargo'
    ]
    success_url = reverse_lazy("funcionario-list")

class FuncionarioUpdateView(UpdateView):
    model = Funcionario
    template_name = 'Funcionarios/funcionario_form.html'
    fields = [
        'nome_funcionario', 'sobrenome_funcionario', 'sexo_funcionario', 'telefone_funcionario', 'data_nascimento_funcionario', 
        'cpf_funcionario', 'rg_funcionario', 'cargo'
    ]
    success_url = reverse_lazy("funcionario-list")

class FuncionarioDeleteView(DeleteView):
    model = Funcionario
    template_name = 'Funcionarios/funcionario_confirm_delete.html'
    success_url = reverse_lazy("funcionario-list")