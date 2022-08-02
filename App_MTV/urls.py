from django.urls import path
from App_MTV import views
from App_MTV.views import vistaInicio,vistaEntrega,vistaComida,vistaClientes,vistaSucursal,formularioSucursal,formularioClientes,formularioComida,formularioEntrega


urlpatterns = [
    path('', views.vistaInicio, name="Inicio"),
    path('sucursal', views.vistaSucursal, name="Sucursal"),
    path('entrega', views.vistaEntrega, name="Entrega"),
    path('comida', views.vistaComida, name="Comida"),
    path('clientes', views.vistaClientes,name="Clientes"),
    #Formularios:
    path('formularioSucursal', views.formularioSucursal,name="FormularioSucursal"),
    path('formularioCliente', views.formularioClientes,name="FormularioClientes"),
    path('formularioComida', views.formularioComida,name="FormularioComida"),
    path('formularioEntrega', views.formularioEntrega,name="FormularioEntrega"),
    
]
