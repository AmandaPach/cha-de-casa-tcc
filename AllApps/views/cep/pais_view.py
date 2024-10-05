from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from AllApps.models.cep.pais_models import Pais
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View, DetailView
from AllApps.myforms import PaisForm
from django.db import IntegrityError


class PaisListView(ListView):
    model = Pais
    template_name = 'Paises\pais_list.html'
    context_object_name = 'paises'

class PaisCreateView(CreateView):
    model = Pais
    template_name = 'Paises\pais_create.html'
    form_class = PaisForm
    success_url = reverse_lazy("pais-list")

    def form_valid(self, form):
        try:
            return super().form_valid(form)
        except IntegrityError as e:
            if 'UNIQUE constraint' in str(e):
                form.add_error('nome_pais', 'Este país já está cadastrado.')
                return self.form_invalid(form)
            else:
                raise e

class PaisUpdateView(UpdateView):
    model = Pais
    template_name = 'Paises/pais_create.html'
    fields = [
       'nome_pais', 'sigla_pais',
    ]
    success_url = reverse_lazy("pais-list")

class PaisDeleteView(DeleteView):
    model = Pais
    template_name = 'Paises/pais_confirm_delete.html'
    success_url = reverse_lazy("pais-list")

# def cadastrar_pais(request):
#     if request.method == 'POST':
#         form = PaisForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('pais-list')
#     else:
#         form = PaisForm()
#     return render(request, 'Paises/pais_create.html', {'form': form})