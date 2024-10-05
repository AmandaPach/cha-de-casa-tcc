from django.shortcuts import render
from django.urls import reverse_lazy
from AllApps.models.cep.cidade_models import Cidade
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View, DetailView

class CidadeListView(ListView):
    model = Cidade
    template_name = 'Cidades\cidade_list.html'
    context_object_name = 'cidades'

class CidadeCreateView(CreateView):
    model = Cidade
    template_name =  'Cidades\cidade_form.html'
    fields = [
       'nome_cidade', 'ddd_cidade', 'estado',
    ]
    success_url = reverse_lazy("cidade-list")

class CidadeUpdateView(UpdateView):
    model = Cidade
    template_name =  'CidadeS\cidade_form.html'
    fields = [
       'nome_cidade', 'ddd_cidade', 'estado',
    ]
    success_url = reverse_lazy("cidade-list")

class CidadeDeleteView(DeleteView):
    model = Cidade
    template_name =  'CidadeS\cidade_confirm_delete.html'
    success_url = reverse_lazy("cidade-list")