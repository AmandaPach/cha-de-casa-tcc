from django.contrib import admin
from django.urls import path, include
from AllApps.views.cep.pais_view import PaisListView, PaisCreateView, PaisUpdateView, PaisDeleteView
from AllApps.views.cep.estado_view import EstadoListView, EstadoCreateView, EstadoUpdateView, EstadoDeleteView
from AllApps.views.cep.cidade_view import CidadeListView, CidadeCreateView, CidadeUpdateView, CidadeDeleteView
from AllApps.views.user.cliente_view import ClienteListView, ClienteCreateView, ClienteUpdateView, ClienteDeleteView
from AllApps.views.user.fornecedor_view import FornecedorListView, FornecedorCreateView, FornecedorUpdateView, FornecedorDeleteView
from AllApps.views.user.cargo_view import CargoListView, CargoCreateView, CargoUpdateView, CargoDeleteView
from AllApps.views.user.funcionario_view import FuncionarioListView, FuncionarioCreateView, FuncionarioUpdateView, FuncionarioDeleteView
from AllApps.views.caixa.formaPagamento_view import FormaPagamentoListView, FormaPagamentoCreateView, FormaPagamentoUpdateView, FormaPagamentoDeleteView
from AllApps.views.caixa.condicaoPagamento_view import CondicaoPagamentoListView, CondicaoPagamentoCreateView, CondicaoPagamentoUpdateView, CondicaoPagamentoDeleteView
from AllApps.views.caixa.produto_view import ProdutoListView, ProdutoCreateView, ProdutoUpdateView, ProdutoDeleteView
from AllApps.views.caixa.tipo_view import TipoListView, TipoCreateView, TipoUpdateView, TipoDeleteView
from AllApps.views.caixa.categoria_view import CategoriaListView, CategoriaCreateView, CategoriaUpdateView, CategoriaDeleteView
from AllApps.views.caixa.compra_view import ComprasListView, ComprasCreateView, ComprasUpdateView, ComprasDeleteView



urlpatterns = [
    path("admin/", admin.site.urls),
   
    path('', PaisListView.as_view(), name='pais-list'),
    path('paises/create', PaisCreateView.as_view(), name='pais-create'),
    path('paises/update/<int:pk>', PaisUpdateView.as_view(), name='pais-update'),
    path('paises/delete/<int:pk>', PaisDeleteView.as_view(), name='pais-delete'),

    path('estados/', EstadoListView.as_view(), name='estado-list'),
    path('estados/create', EstadoCreateView.as_view(), name='estado-create'),
    path('estados/update/<int:pk>', EstadoUpdateView.as_view(), name='estado-update'),
    path('estados/delete/<int:pk>', EstadoDeleteView.as_view(), name='estado-delete'),

    path('cidades/', CidadeListView.as_view(), name='cidade-list'),
    path('cidades/create', CidadeCreateView.as_view(), name='cidade-create'),
    path('cidades/update/<int:pk>', CidadeUpdateView.as_view(), name='cidade-update'),
    path('cidades/delete/<int:pk>', CidadeDeleteView.as_view(), name='cidade-delete'),

    path('clientes/', ClienteListView.as_view(), name='cliente-list'),
    path('clientes/create', ClienteCreateView.as_view(), name='cliente-create'),
    path('clientes/update/<int:pk>', ClienteUpdateView.as_view(), name='cliente-update'),
    path('clientes/delete/<int:pk>', ClienteDeleteView.as_view(), name='cliente-delete'),

    path('fornecedores/', FornecedorListView.as_view(), name='fornecedor-list'),
    path('fornecedores/create', FornecedorCreateView.as_view(), name='fornecedor-create'),
    path('fornecedores/update/<int:pk>', FornecedorUpdateView.as_view(), name='fornecedor-update'),
    path('fornecedores/delete/<int:pk>', FornecedorDeleteView.as_view(), name='fornecedor-delete'),

    path('cargos/', CargoListView.as_view(), name='cargo-list'),
    path('cargos/create', CargoCreateView.as_view(), name='cargo-create'),
    path('cargos/update/<int:pk>', CargoUpdateView.as_view(), name='cargo-update'),
    path('cargos/delete/<int:pk>', CargoDeleteView.as_view(), name='cargo-delete'),

    path('funcionarios/', FuncionarioListView.as_view(), name='funcionario-list'),
    path('funcionarios/create', FuncionarioCreateView.as_view(), name='funcionario-create'),
    path('funcionarios/update/<int:pk>', FuncionarioUpdateView.as_view(), name='funcionario-update'),
    path('funcionarios/delete/<int:pk>', FuncionarioDeleteView.as_view(), name='funcionario-delete'),

    path('formasPagamento/', FormaPagamentoListView.as_view(), name='formaPagamento-list'),
    path('formasPagamento/create', FormaPagamentoCreateView.as_view(), name='formaPagamento-create'),
    path('formasPagamento/update/<int:pk>', FormaPagamentoUpdateView.as_view(), name='formaPagamento-update'),
    path('formasPagamento/delete/<int:pk>', FormaPagamentoDeleteView.as_view(), name='formaPagamento-delete'),

    path('condicoesPagamento/', CondicaoPagamentoListView.as_view(), name='condicaoPagamento-list'),
    path('condicoesPagamento/create',  CondicaoPagamentoCreateView.as_view(), name='condicaoPagamento-create'),
    path('condicoesPagamento/update/<int:pk>', CondicaoPagamentoUpdateView.as_view(), name='condicaoPagamento-update'),
    path('condicoesPagamento/delete/<int:pk>', CondicaoPagamentoDeleteView.as_view(), name='condicaoPagamento-delete'),

    path('produto/', ProdutoListView.as_view(), name='produto-list'),
    path('produto/create', ProdutoCreateView.as_view(), name='produto-create'),
    path('produto/update/<int:pk>', ProdutoUpdateView.as_view(), name='produto-update'),
    path('produto/delete/<int:pk>', ProdutoDeleteView.as_view(), name='produto-delete'),

    path('categoria/', CategoriaListView.as_view(), name='categoria-list'),
    path('categoria/create', CategoriaCreateView.as_view(), name='categoria-create'),
    path('categoria/update/<int:pk>', CategoriaUpdateView.as_view(), name='categoria-update'),
    path('categoria/delete/<int:pk>', CategoriaDeleteView.as_view(), name='categoria-delete'),

    path('tipo/', TipoListView.as_view(), name='tipo-list'),
    path('tipo/create', TipoCreateView.as_view(), name='tipo-create'),
    path('tipo/update/<int:pk>', TipoUpdateView.as_view(), name='tipo-update'),
    path('tipo/delete/<int:pk>', TipoDeleteView.as_view(), name='tipo-delete'),

    path('compra/', ComprasListView.as_view(), name='compra-list'),
    path('compra/create', ComprasCreateView.as_view(), name='compra-create'),
    path('compra/update/<int:pk>', ComprasUpdateView.as_view(), name='compra-update'),
    path('compra/delete/<int:pk>', ComprasDeleteView.as_view(), name='compra-delete'),
]