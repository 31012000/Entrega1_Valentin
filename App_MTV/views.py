
from django.http import HttpResponse
from App_MTV.models import Sucursal
from django.shortcuts import render 
from App_MTV.forms import formularioSucursal

# Create your views here.

def vistaInicio(request):

    return render(request,"inicio.html")

def vistaSucursal(request):

    return render(request,"sucursal.html")

def vistaClientes(request):

    return render(request,"clientes.html")
def vistaComida(request):

    return render(request,"comida.html")

def vistaEntrega(request):

    return render(request,"entrega.html")         

#Creacion de Formularios:
###################################################################################################
def formularioSucursal(request):
    
    if request.method == 'POST':

        miFormulario = formularioSucursal(request.POST)

        if miFormulario.is_valid:

            data = miFormulario.cleaned_data

            sucursal = Sucursal(direccion=data['Direccion'],horario=data['Horario'],cantidad_empleados=data['Empleados']) # IMPORTANTE LAS KEY
        
            sucursal.save()

            return render(request,"inicio.html")
    
    else:
        
        miFormulario = formularioSucursal()

    return render(request,"sucursal.html",{"formularioSucursal": miFormulario })    
     
    
       









def formularioClientes(request):

    return render(request,"clientes.html")


def formularioComida(request):

    return render(request,"comida.html")


def formularioEntrega(request):

    return render(request,"entrega.html")      
