from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View, DetailView, FormView
from AllApps.models.caixa.compra_models import Compras
from AllApps.forms.caixa.compra_forms import ComprasForm
from django.db import IntegrityError
from django.template.loader import render_to_string
from django.http import JsonResponse

class ComprasListView(ListView):
    model = Compras
    template_name = 'Compras/compra_list.html'
    context_object_name = 'compras'
    form = ComprasForm

class ComprasCreateView(FormView):
    model = Compras
    template_name = 'Compras/compra_form.html'
    form_class = ComprasForm
    success_url = reverse_lazy("compra-list")
    
    def abre_modal(self, request):
        form = ComprasForm()
        context = {
            'form': form,
        }

        return JsonResponse({
            'data': render_to_string('Compras/compra_form.html', context)
        })


    # def form_valid(self, form):
    #     try:
    #         return super().form_valid(form)
    #     except IntegrityError as e:
    #         if 'UNIQUE constraint' in str(e):
    #             form.add_error('produto_id.nome_produto', 'Essa nota está cadastrado.')
    #             return self.form_invalid(form)
    #         else:
    #             raise e

class ComprasUpdateView(UpdateView):
    model = Compras
    template_name = 'Compras/compra_form.html'
    form_class = ComprasForm
    success_url = reverse_lazy("compra-list")

#     def form_valid(self, form):
#         try:
#             return super().form_valid(form)
#         except IntegrityError as e:
#             if 'UNIQUE constraint' in str(e):
#                 form.add_error('nome_produto', 'Este produto já está cadastrado.')
#                 return self.form_invalid(form)
#             else:
#                 raise e

class ComprasDeleteView(DeleteView):
    model = Compras
    template_name = 'Compras/compra_confirm_delete.html'
    success_url = reverse_lazy("compra-list")

# class ComprasModal(CreateView):
#     model = Compras
#     template_name = 'Compras/compras_form.html'
#     form_class = ComprasForm
    
