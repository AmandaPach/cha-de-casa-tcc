from django.shortcuts import render
from django.urls import reverse_lazy
from AllApps.models.cep.estado_models import Estado
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View, DetailView
from django.db import IntegrityError


class EstadoListView(ListView):
    model = Estado
    template_name = 'Estados\estado_list.html'
    context_object_name = 'estados'

class EstadoCreateView(CreateView):
    model = Estado
    template_name =  'Estados\estado_form.html'
    fields = [
       'nome_estado', 'sigla_estado', 'pais'
    ]
    success_url = reverse_lazy("estado-list")
    
    def form_valid(self, form):
        try:
            return super().form_valid(form)
        except IntegrityError as e:
            if 'UNIQUE constraint' in str(e):
                form.add_error('nome_estado', 'Este estado já está cadastrado.')
                return self.form_invalid(form)
            else:
                raise e


    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["Paises"] = Pais.objects.all()
    #     return context
    

class EstadoUpdateView(UpdateView):
    model = Estado
    template_name =  'Estados\estado_form.html'
    fields = [
       'nome_estado', 'sigla_estado', 'pais',
    ]
    success_url = reverse_lazy("estado-list")

class EstadoDeleteView(DeleteView):
    model = Estado
    template_name =  'Estados\estado_confirm_delete.html'
    success_url = reverse_lazy("estado-list")